import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

    while True:
        print("\nMain Menu:")
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")

        choice = input("Nhập lựa chọn của bạn (1-5): ")

        if choice == '1':
            cursor.execute("SELECT * FROM Names")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        elif choice == '2':
            first_name = input("First Name: ")
            last_name = input("Surname: ")
            phone_number = input("Phone Number: ")
            cursor.execute("INSERT INTO Names (FirstName, SurName, PhoneNumber) VALUES (?, ?, ?)",
                           (first_name, last_name, phone_number))
            db.commit()
            print("them moi thanh cong!")

        elif choice == '3':
            last_name = input("nhap ho can tim: ")
            cursor.execute("SELECT * FROM Names WHERE SurName=?", (last_name,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)

        elif choice == '4':
            id = int(input("nhap id muon xoa: "))
            cursor.execute("DELETE FROM Names WHERE ID=?", (id,))
            db.commit()
            print(f"da xoa id {id}")

        elif choice == '5':
            print("Bye!")
            break

        else:
            print("chon sai hay thu lai.")
