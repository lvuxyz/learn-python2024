import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="countries"
)

mycursor = mydb.cursor()

mycursor.execute("""
    CREATE TABLE countries (
        country_id INT PRIMARY KEY,
        country_name VARCHAR(100) NOT NULL,
        region_id INT
    )
""")
