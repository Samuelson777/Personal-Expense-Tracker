import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',  # replace with your MySQL username
        password='your_password',  # replace with your MySQL password
        database='expense_tracker'
    )
    return connection

def add_expense(amount, date, category_id, description):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Expenses (amount, date, category_id, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (amount, date, category_id, description))
        connection.commit()
        print("Expense added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def view_expenses():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT e.expense_id, e.amount, e.date, c.category_name, e.description FROM Expenses e JOIN Categories c ON e.category_id = c.category_id"
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(f"ID: {row[0]}, Amount: {row[1]}, Date: {row[2]}, Category: {row[3]}, Description: {row[4]}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_categories():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        query = "SELECT category_id, category_name FROM Categories"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            categories = get_categories()
            print("Available Categories:")
            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}")
            category_id = int(input("Enter category ID: "))
            description = input("Enter description: ")
            add_expense(amount, date, category_id, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()