-- Database schema (sample)
CREATE TABLE Users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE FIRs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    fir_number VARCHAR(50) NOT NULL UNIQUE,
    crime_type VARCHAR(100),
    district VARCHAR(100),
    police_station VARCHAR(200),
    incident_date DATE,
    details TEXT
);
