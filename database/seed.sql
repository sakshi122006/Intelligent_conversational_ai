-- Minimal seed data for development

INSERT INTO users (username, password_hash, role) VALUES ('admin', 'changeme', 'Admin');

INSERT INTO firs (fir_number, complainant_name, crime_type, district, police_station, incident_date, details) VALUES
('FIR-2026-0001', 'R. Kumar', 'Theft', 'Bangalore', 'Central', '2026-07-01', 'Bike stolen from market'),
('FIR-2026-0002', 'S. Rao', 'Assault', 'Mysore', 'North', '2026-07-05', 'Physical assault reported');
