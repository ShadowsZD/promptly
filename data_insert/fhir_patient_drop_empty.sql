INSERT INTO fhir_patient (id, full_name, birth_date, gender, address, telecom, marital_status, insurance_number, nationality)
	SELECT 
		md5(CONCAT(first_name, last_name, birth_date, address, phone_number, email)) as id,
		CONCAT(first_name, ' ', last_name) as full_name,
		birth_date,
		gender,
		address,
		jsonb_build_object('phone', phone_number, 'email', email) as telecom,
		marital_status,
		insurance_number,
		nationality
	FROM raw_patient
	WHERE birth_date IS NOT NULL 
	AND address IS NOT NULL
    AND email ~ '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$';