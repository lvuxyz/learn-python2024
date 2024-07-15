import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="countries"
)

mycursor = mydb.cursor()
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        job_id INT PRIMARY KEY,
        job_title VARCHAR(100) NOT NULL,
        min_salary DECIMAL(10, 2),
        max_salary DECIMAL(10, 2)
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS job_history (
        employee_id INT PRIMARY KEY,
        start_date DATE,
        end_date DATE,
        job_id INT,
        department_id INT,
        CONSTRAINT fk_job_id FOREIGN KEY (job_id) REFERENCES jobs(job_id)
    )
""")

mydb.close()
