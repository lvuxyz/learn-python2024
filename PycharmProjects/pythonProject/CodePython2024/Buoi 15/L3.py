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
            country_name VARCHAR(100) NOT NULL CHECK (country_name IN ('Italy', 'India', 'China')),
            region_id INT
        )
    """)

sql_insert_india = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
val_india = (2, 'India', 2)
mycursor.execute(sql_insert_india, val_india)

sql_insert_china = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
val_china = (3, 'China', 3)
mycursor.execute(sql_insert_china, val_china)

sql_insert_italy = "INSERT INTO countries (country_id, country_name, region_id) VALUES (%s, %s, %s)"
val_italy = (4, 'Italy', 4)
mycursor.execute(sql_insert_italy, val_italy)

mydb.commit()
