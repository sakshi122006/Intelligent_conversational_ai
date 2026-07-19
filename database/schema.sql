-- Schema for KSP Crime Intelligence (minimal starter)

CREATE TABLE users (
    id INT IDENTITY PRIMARY KEY,
    username NVARCHAR(100) NOT NULL UNIQUE,
    password_hash NVARCHAR(255) NOT NULL,
    role NVARCHAR(50) NOT NULL,
    created_at DATETIME2 DEFAULT GETDATE()
);

CREATE TABLE firs (
    id INT IDENTITY PRIMARY KEY,
    fir_number NVARCHAR(50) NOT NULL UNIQUE,
    complainant_name NVARCHAR(200),
    crime_type NVARCHAR(100),
    district NVARCHAR(100),
    police_station NVARCHAR(200),
    incident_date DATE,
    details NVARCHAR(MAX),
    created_at DATETIME2 DEFAULT GETDATE()
);

CREATE TABLE crimes (
    id INT IDENTITY PRIMARY KEY,
    fir_id INT FOREIGN KEY REFERENCES firs(id),
    criminal_name NVARCHAR(200),
    status NVARCHAR(50),
    latitude FLOAT NULL,
    longitude FLOAT NULL
);

CREATE TABLE chat_history (
    id INT IDENTITY PRIMARY KEY,
    user_id INT FOREIGN KEY REFERENCES users(id),
    message NVARCHAR(MAX),
    response NVARCHAR(MAX),
    language NVARCHAR(10),
    created_at DATETIME2 DEFAULT GETDATE()
);

CREATE TABLE audit_logs (
    id INT IDENTITY PRIMARY KEY,
    user_id INT NULL,
    action NVARCHAR(200),
    metadata NVARCHAR(MAX),
    created_at DATETIME2 DEFAULT GETDATE()
);
