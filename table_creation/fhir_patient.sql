CREATE TABLE fhir_patient (
    id VARCHAR(255) PRIMARY KEY, -- Unique ID generated from patient attributes
    full_name VARCHAR(200),
    birth_date DATE,
    gender VARCHAR(20),
    address VARCHAR(255),
    telecom JSONB, -- JSON object with two fields, phone and email
    marital_status VARCHAR(20),
    insurance_number VARCHAR(255),
    nationality VARCHAR(20)
);