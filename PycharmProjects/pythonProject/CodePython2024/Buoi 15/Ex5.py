import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="countries"
)

mycursor = mydb.cursor()

mycursor.execute("""
    INSERT INTO jobs (job_id, job_title, min_salary, max_salary)
    VALUES (1, 'Software Engineer', 30000, 80000)
    ON DUPLICATE KEY UPDATE
    job_title = VALUES(job_title), min_salary = VALUES(min_salary), max_salary = VALUES(max_salary)
""")
mydb.commit()

mydb.close()
