# Smart Waste Management & Bin Level Detection System

An Industry-Oriented IoT Project for Real-Time Waste Monitoring, Smart Collection Decision Support, and Smart City Waste Management using ESP32, MQTT, SQLite, and Streamlit.

---

## Project Overview

Traditional waste collection systems follow fixed schedules regardless of whether a garbage bin is empty, half-full, or overflowing. This often results in:

- Unnecessary collection trips
- Increased fuel consumption
- Higher operational costs
- Overflowing bins
- Poor sanitation management
- Inefficient resource utilization

This project solves these problems by continuously monitoring the fill level of a waste bin and providing real-time visibility through an analytics dashboard.

The system uses an ultrasonic sensor to measure the waste level inside a bin, processes the data using an ESP32 microcontroller, transmits information through MQTT, stores records in SQLite, and visualizes insights using a Streamlit dashboard.

The result is a smart waste management platform that can help municipalities, campuses, airports, malls, railway stations, and smart city operators optimize waste collection operations.

---

# Key Features

- Real-Time Bin Monitoring
- Fill Percentage Calculation
- Waste Level Classification
- MQTT-Based IoT Communication
- SQLite Data Storage
- Streamlit Dashboard
- Alert Generation
- Historical Data Tracking
- Smart Bin Visualization
- Fill Level Gauge
- Alert History Tracking
- Collection Recommendation Logic
- System Health Monitoring
- Industry-Oriented Architecture
- Wokwi Hardware Simulation
- Beginner-Friendly Implementation

---

# Technology Stack

## Hardware Layer

- ESP32
- HC-SR04 Ultrasonic Sensor
- OLED Display
- LED Indicators
- Buzzer

## Simulation

- Wokwi Simulator
- PlatformIO

## Communication

- MQTT
- HiveMQ Broker

## Backend

- Python

## Database

- SQLite

## Dashboard

- Streamlit
- Plotly
- Pandas

---

# Real World Applications

This type of system is used in:

## Smart Cities

Monitoring public waste bins across urban areas.

## Municipal Corporations

Reducing collection costs and optimizing routes.

## Airports

Monitoring waste accumulation in terminals.

## Railway Stations

Preventing overflowing bins in high-traffic areas.

## Shopping Malls

Improving cleanliness and waste management.

## University Campuses

Managing waste collection across multiple buildings.

## Waste Collection Companies

Providing data-driven collection schedules.

---

# System Architecture

```text
+-----------------------+
| Garbage Bin           |
+-----------+-----------+
            |
            v
+-----------------------+
| HC-SR04 Sensor        |
| Distance Measurement  |
+-----------+-----------+
            |
            v
+-----------------------+
| ESP32                 |
| Fill Calculation      |
| Alert Logic           |
+-----------+-----------+
            |
            | MQTT Publish
            v
+-----------------------+
| MQTT Broker           |
| HiveMQ                |
+-----------+-----------+
            |
            | MQTT Subscribe
            v
+-----------------------+
| Python Backend        |
| Data Processing       |
+-----------+-----------+
            |
            v
+-----------------------+
| SQLite Database       |
+-----------+-----------+
            |
            v
+-----------------------+
| Streamlit Dashboard   |
+-----------+-----------+
            |
            v
+-----------------------+
| Analytics & Alerts    |
+-----------------------+
```

---

# Working Principle

The ultrasonic sensor continuously measures the distance between the sensor and the waste level.

Example:

```text
Bin Height = 40 cm

Measured Distance = 10 cm

Fill Percentage =
((40 - 10) / 40) × 100

Fill Percentage = 75%
```

The ESP32 calculates:

- Distance
- Fill Percentage
- Bin Status
- Alert State

and publishes the data through MQTT.

The backend receives this information and stores it inside SQLite.

The dashboard visualizes the data in real time.

---

# Bin Status Classification

| Fill Percentage | Status |
|---------------|---------|
| 0 - 25% | Empty |
| 26 - 60% | Half Full |
| 61 - 85% | Almost Full |
| 86 - 100% | Full |

---

# Alert Logic

| Fill Percentage | Alert |
|----------------|--------|
| Below 85% | No Alert |
| Above 85% | Collection Required |

---

# Project Structure

```text
Smart-Waste-Management-Bin-Level-Detection-System/

│
├── backend/
│   ├── mqtt_subscriber.py
│   ├── database_manager.py
│   └── config.py
│
├── dashboard/
│   ├── app.py
│   ├── utils.py
│   └── components/
│
├── database/
│   ├── waste_management.db
│   ├── schema.sql
│   └── database_setup.py
│
├── Smart_Waste_Management_ESP32_Code/
│   ├── src/
│   ├── include/
│   ├── platformio.ini
│   └── wokwi.toml
│
├── images/
│
├── docs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Dashboard Features

The dashboard provides:

## Real-Time Monitoring

Displays current:

- Fill Percentage
- Distance
- Status
- Alert State

## Fill Level Gauge

Visual representation of waste level.

## Smart Bin Visualization

Shows approximate waste accumulation.

## Alert History

Tracks all critical events.

## Historical Analytics

Displays trends over time.

## System Health

Monitors:

- ESP32 Status
- MQTT Connection
- Database Connection
- Dashboard Status

---

# Database Design

Table:

```sql
waste_readings
```

Columns:

| Column | Description |
|----------|-------------|
| id | Unique Record ID |
| timestamp | Reading Time |
| bin_id | Bin Identifier |
| distance | Measured Distance |
| fill_percentage | Fill Level |
| status | Current Status |
| alert | Alert State |

---

# MQTT Message Format

Example:

```json
{
  "bin_id": "BIN-01",
  "distance": 10.08,
  "fill_percentage": 74.79,
  "status": "ALMOST_FULL",
  "alert": false
}
```

---

# Screenshots

Refer screenshots inside the images folder.

---

# How To Run This Project

This section is intentionally written for absolute beginners.

---

# Prerequisites

Install:

## Windows

1. Python 3.12+
2. VS Code
3. Git
4. PlatformIO Extension
5. Wokwi Extension

## macOS

Install:

1. Python 3.12+
2. VS Code
3. Git
4. PlatformIO Extension
5. Wokwi Extension

Verify:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Waste-Management-Bin-Level-Detection-System.git
```

Enter project:

```bash
cd Smart-Waste-Management-Bin-Level-Detection-System
```

---

# Step 2: Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

macOS:

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Step 4: Create Database

Run:

```bash
python database/database_setup.py
```

Expected:

```text
Database Created Successfully
```

---

# Step 5: Start MQTT Subscriber

Open a terminal.

Run:

```bash
python backend/mqtt_subscriber.py
```

Expected:

```text
Connected
Subscribed to smartbin/bin01
```

Leave this terminal running.

---

# Step 6: Start ESP32 Simulation

Open:

```text
Smart_Waste_Management_ESP32_Code
```

Run Wokwi Simulation.

Move the virtual object to simulate waste levels.

ESP32 will begin publishing MQTT messages.

---

# Step 7: Launch Dashboard

Open another terminal.

Run:

```bash
streamlit run dashboard/app.py
```

Browser will open automatically.

Dashboard URL:

```text
http://localhost:8501
```

---

# Step 8: Test The System

Move the Wokwi slider.

Observe:

- Distance changes
- Fill Percentage changes
- Status changes
- Database updates
- Dashboard updates

---

# Expected Workflow

```text
Move Waste Level
        ↓
HC-SR04 Reads Distance
        ↓
ESP32 Calculates Fill %
        ↓
MQTT Sends Data
        ↓
Python Receives Data
        ↓
SQLite Stores Data
        ↓
Dashboard Updates
```

---

# Future Enhancements

- Multiple Smart Bins
- Route Optimization
- Email Notifications
- SMS Alerts
- Predictive Waste Collection
- Mobile Application
- Cloud Deployment
- Node-RED Integration
- Machine Learning Forecasting

---

# Learning Outcomes

This project demonstrates:

- Internet of Things (IoT)
- Embedded Systems
- ESP32 Programming
- Sensor Interfacing
- MQTT Communication
- Backend Development
- Database Management
- Dashboard Development
- Data Visualization
- Real-Time Monitoring Systems

---

# Author

Aniket Satpathy

Industry-Oriented IoT Project

Smart Waste Management & Bin Level Detection System

---

# License

This project is developed for educational, research, and portfolio purposes.
