import sqlite3

connect = sqlite3.connect("employee.db")
cursor = connect.cursor()

def table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emplyee (
            Name TEXT,
            ID INTEGER,
            Age INTEGER,
            Salary INTEGER,
            Position Text );
    ''')
    print("Table Created Successfully")
    connect.commit()

def data_employee():
    print("Input the employee data")
    name = input("Enter Name: ")
    id = int(input("Enter ID: "))
    age = int(input("Enter Age: "))
    salary = int(input("Enter Salary"))
    position = input("Enter Position: ")

    cursor.execute(
        '''INSERT INTO emplyee (Name, ID, Age, Salary, Position) VALUES (?, ?, ?, ?, ?)''',
        (name, id, age, salary, position))
    print("Data Created Successfully")
    connect.commit()

def view_employee():
    cursor.execute('''SELECT * FROM emplyee''')
    print("The data of employees are: ")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_employee():
    id = int(input("Enter ID to update: "))
    name = input("Enter new Name: ")
    age = int(input("Enter updated age: "))
    salary = int(input("Enter updated Salary"))
    position = input("Enter updated Position: ")

    cursor.execute(
        '''UPDATE emplyee SET Name = ?, Age = ?, Salary = ?, Position = ? WHERE ID = ?''',
        (name, age, salary, position, id) )
    print("Data Updated Successfully")
    connect.commit()

def delete_employee():
    id = int(input("Enter ID to delete: "))
    cursor.execute('''DELETE FROM emplyee WHERE ID = ?''', (id,) )
    print("Data Deleted Successfully")
    connect.commit()

def main():
    table()  
    while True:
        print("1. Add Employee\n 2. View Employees\n3. Update Employee \n4. Delete Employee \n5. Exit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                data_employee()
            case 2:
                view_employee()
            case 3:
                update_employee()
            case 4:
                delete_employee()
            case 5:
                print("Exiting Program...")
                connect.close()
                break
            case _:
                print("Invalid choice")

main()

