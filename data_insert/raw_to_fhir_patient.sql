INSERT INTO fhir_patient (id, full_name, birth_date, gender, address, telecom, marital_status, insurance_number, nationality)
	SELECT 
		md5(CONCAT(first_name, last_name, birth_date, address, phone_number, email)) as id,
		CONCAT(first_name, ' ', last_name) as full_name,
		COALESCE(birth_date, '1900-01-01') AS birth_date,
		gender,
		COALESCE(address, 'N/A') as address,
		jsonb_build_object('phone', phone_number, 'email', email) as telecom,
		marital_status,
		insurance_number,
		nationality
	FROM raw_patient;
