import psycopg2
from config import conn

config = psycopg2.connect(**conn)

cur = config.cursor()

# 1
def returns_data():
    field = input("Enter the field to query (name/number/all): ")
    if field == "name":
        name = input("Enter the name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE name = %s",
            (name,)
        )
    elif field == "number":
        phone = input("Enter the phone: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE number = %s",
            (phone,)
        )
    elif field == "all":
        cur.execute("SELECT * FROM phonebook")
    else:
        print("ERROR")
        return
    rows = cur.fetchall()
    for row in rows:
        print(row)

# 2
def insert_data_from_console():
    name = input("Enter name: ")
    number = input("Enter phone: ")
    cur.execute(
        'INSERT INTO phonebook(name,number) VALUES(%s,%s)',
        (name,number)
    )
    config.commit()
    print("Data uploaded successfully from console.")


# 2
def update_data():
    name = input("Enter the name of the user to update: ")
    field = input("Enter the field to update (name/phone): ")
    value = input("Enter the new value: ")
    if field == "name":
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (value, name)
        )
    elif field == "phone":
        cur.execute(
            "UPDATE phonebook SET number = %s WHERE name = %s",
            (value, name)
        )
    config.commit()
    print("Data updated successfully.")



# 3
def insert_many_users():
    users = []
    while True:
        name = input("Enter a name (or press enter to finish): ")
        if not name:
            break
        phone = input("Enter a phone number: ")
        users.append((name, phone))

    invalid_data = []
    for user1 in users:
        name, phone = user1
        if len(phone) != 11 or not phone.isdigit():
            invalid_data.append(user1)
        else:
            cur.execute(
                "INSERT INTO phonebook(name, number) VALUES (%s, %s)",
                (name, phone)
            )
    config.commit()
    if invalid_data:
        print("The following data was invalid and could not be inserted:")
        for user2 in invalid_data:
            print(user2)
    else:
        print("All data was inserted successfully.")


# 4
def query_data_with_pagination():
    limit = input("Enter the number of rows to retrieve: ")
    offset = input("Enter the starting row number: ")
    if limit and offset:
        cur.execute(
            "SELECT * FROM phonebook ORDER BY name LIMIT %s OFFSET %s",
            (limit, offset)
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
    else:
        print("Error: Please enter valid limit and offset values.")


# 5
def delete_data():
    field = input("Enter the field to delete by (name/number): ")
    value = input("Enter the value: ")
    if field == "name":
        cur.execute(
            "DELETE FROM phonebook WHERE name = %s",
            (value,)
        )
    elif field == "number":
        cur.execute(
            "DELETE FROM phonebook WHERE number = %s",
            (value,)
        )
    config.commit()
    print("Data deleted successfully.")


# Main program loop
while True:
    print("PhoneBook options:")
    print("1. Returns data.")
    print("2. Insert data from console.")
    print("3. Update data.")
    print('4. Insert many users.')
    print('5. Query data with pagination')
    print("6. Delete data.")
    print("7. Exit.")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        returns_data()
    elif choice == "2":
        insert_data_from_console()
    elif choice == "3":
        update_data()
    elif choice=="4":
        insert_many_users()
    elif choice == "5":
        query_data_with_pagination()
    elif choice == "6":
        delete_data()
    elif choice == "7":
        break
    else:
        print("Invalid input. Please enter a valid option.")
config.commit()
cur.close()
config.close()