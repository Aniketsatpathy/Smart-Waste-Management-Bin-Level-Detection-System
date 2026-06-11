#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <ArduinoJson.h>
#include <PubSubClient.h>
#include <WiFi.h>
#include <Wire.h>

#include "../include/mqtt_config.h"
#include "../include/sensor_config.h"
#include "../include/wifi_config.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define SCREEN_ADDRESS 0x3C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

WiFiClient espClient;
PubSubClient mqttClient(espClient);

// --------------------------------------------------
// Connect WiFi
// --------------------------------------------------

void connectWiFi() {
  Serial.println();
  Serial.println("Connecting WiFi...");

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi Connected");

  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

// --------------------------------------------------
// Connect MQTT
// --------------------------------------------------

void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.println("Connecting MQTT...");

    String clientId = "SmartBin-";

    clientId += String(random(1000));

    if (mqttClient.connect(clientId.c_str())) {
      Serial.println("MQTT Connected");
    } else {
      Serial.print("Failed. State=");

      Serial.println(mqttClient.state());

      delay(2000);
    }
  }
}

// --------------------------------------------------
// Read Distance
// --------------------------------------------------

float getDistanceCM() {
  digitalWrite(TRIG_PIN, LOW);

  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);

  delayMicroseconds(10);

  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duration == 0) {
    return BIN_HEIGHT_CM;
  }

  float distance = duration * 0.0343 / 2.0;

  return distance;
}

// --------------------------------------------------
// Fill Percentage
// --------------------------------------------------

float calculateFillLevel(float distance) {
  float fillLevel = ((BIN_HEIGHT_CM - distance) / BIN_HEIGHT_CM) * 100.0;

  if (fillLevel < 0) {
    fillLevel = 0;
  }

  if (fillLevel > 100) {
    fillLevel = 100;
  }

  return fillLevel;
}

// --------------------------------------------------
// Bin Status
// --------------------------------------------------

String getStatus(float fillLevel) {
  if (fillLevel <= 25) {
    return "EMPTY";
  }

  if (fillLevel <= 60) {
    return "HALF_FULL";
  }

  if (fillLevel <= 85) {
    return "ALMOST_FULL";
  }

  return "FULL";
}

// --------------------------------------------------
// Alert
// --------------------------------------------------

bool isAlertActive(float fillLevel) { return fillLevel >= ALERT_THRESHOLD; }

// --------------------------------------------------
// Publish MQTT
// --------------------------------------------------

void publishData(float distance, float fillLevel, String status, bool alert) {
  JsonDocument doc;

  doc["bin_id"] = "BIN-01";

  doc["distance"] = round(distance * 100) / 100;

  doc["fill_percentage"] = round(fillLevel * 100) / 100;

  doc["status"] = status;

  doc["alert"] = alert;

  String payload;

  serializeJson(doc, payload);

  mqttClient.publish(MQTT_TOPIC, payload.c_str());

  Serial.println();
  Serial.println("Published MQTT:");

  Serial.println(payload);
}

// --------------------------------------------------
// Setup
// --------------------------------------------------

void setup() {
  Serial.begin(115200);

  pinMode(TRIG_PIN, OUTPUT);

  pinMode(ECHO_PIN, INPUT);

  // Initialize SSD1306 OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 OLED allocation failed"));
  } else {
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(0, 10);
    display.println("Smart Waste System");
    display.println("Initializing...");
    display.display();
  }

  connectWiFi();

  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
}

// --------------------------------------------------
// Update OLED Display
// --------------------------------------------------

void updateDisplay(float distance, float fillLevel, String status, bool alert) {
  display.clearDisplay();

  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);

  display.setCursor(0, 0);
  display.println("SMART WASTE BIN");
  display.println("---------------------");

  display.print("Distance: ");
  display.print(distance, 1);
  display.println(" cm");

  display.print("Fill Level: ");
  display.print(fillLevel, 1);
  display.println(" %");

  display.print("Status: ");
  display.println(status);

  if (alert) {
    display.println();
    display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Inverted text
    display.print(" !!! BIN FULL !!! ");
  }

  display.display();
}

// --------------------------------------------------
// Loop
// --------------------------------------------------

void loop() {
  if (!mqttClient.connected()) {
    connectMQTT();
  }

  mqttClient.loop();

  float distance = getDistanceCM();

  float fillLevel = calculateFillLevel(distance);

  String status = getStatus(fillLevel);

  bool alert = isAlertActive(fillLevel);

  Serial.println("------------------");

  Serial.print("Distance: ");

  Serial.print(distance);

  Serial.println(" cm");

  Serial.print("Fill Level: ");

  Serial.print(fillLevel);

  Serial.println("%");

  Serial.print("Status: ");

  Serial.println(status);

  Serial.print("Alert: ");

  Serial.println(alert);

  updateDisplay(distance, fillLevel, status, alert);

  publishData(distance, fillLevel, status, alert);

  delay(5000);
}