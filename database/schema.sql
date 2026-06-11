CREATE TABLE IF NOT EXISTS waste_readings (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

    bin_id TEXT NOT NULL,

    distance REAL NOT NULL,

    fill_percentage REAL NOT NULL,

    status TEXT NOT NULL,

    alert INTEGER NOT NULL

);