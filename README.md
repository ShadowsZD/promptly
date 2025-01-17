# Promptly Exercise

This is a code solving the exercise provided

## Requirements
Clone the repo, then install requirements

```bash
pip install -r requirements.txt
```

## Explanation
### Table Creation Folder
Contains SQL files with definition of tables provided, blood_type was changed from VARCHAR(5) to fit for entry with Value unknown on raw table.

### Data Insert Folder
Contains SQL files with the transformation to FHIR format
- raw_to_fhir_patient: coalesces address and birth date to default value if null 
- fhir_patient_drop_empty: drop rows when address or birthdate is empty or if email is invalid

## Usage
Definitions for the database are coded on the start of python file
```python
HOST = "localhost"
PORT = 5432
USER = "test_user"
PASSWORD = "test_pass"
DB_NAME = "test_db"
```
To run the code
```bash
python main.py
```
If you have to run only some of the steps you can comment whatever you dont need under main()

```python
#create_db(DB_NAME)

#create_table(DB_NAME, "table_creation/raw_patient.sql")
#insert_csv(DB_NAME, "patient.csv", "raw_patient")

create_table(DB_NAME, "table_creation/fhir_patient.sql")
#insert_sql(DB_NAME, "data_insert/fhir_patient_drop_empty.sql") 
insert_sql(DB_NAME, "data_insert/raw_to_fhir_patient.sql")  
```

## Details

RegEx for email validation used from [StackExchange](https://dba.stackexchange.com/questions/68266/what-is-the-best-way-to-store-an-email-address-in-postgresql/165923#165923)
