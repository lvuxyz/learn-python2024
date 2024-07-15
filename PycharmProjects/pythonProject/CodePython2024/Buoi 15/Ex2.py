import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="countries"
)

mycursor = mydb.cursor()

mycursor.execute("""
    INSERT INTO countries (country_id, country_name)
    VALUES (2, 'Japan')
""")
mydb.commit()

mydb.close()
