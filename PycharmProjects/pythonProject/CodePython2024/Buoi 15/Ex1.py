import mysql.connector

# Kết nối đến cơ sở dữ liệu
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="countries"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS countries")

# Tạo bảng countries
mycursor.execute("""
    CREATE TABLE countries (
        country_id INT PRIMARY KEY,
        country_name VARCHAR(100) NOT NULL,
        region_id INT
    )
""")

try:
    mycursor.execute("""
        INSERT INTO countries (country_id, country_name, region_id)
        VALUES (1, 'Vietnam', 10)
    """)
    mydb.commit()
    print("Bản ghi đã được chèn thành công.")
except mysql.connector.Error as err:
    print(f"Lỗi: {err}")
mydb.close()
