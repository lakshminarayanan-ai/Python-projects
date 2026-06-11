
# Student Management System (Python)
# Simple console-based project

students = []

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    students.append({"roll": roll, "name": name, "dept": dept})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll No: {s['roll']} | Name: {s['name']} | Department: {s['dept']}")
    print()

def search_student():
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Found -> Name: {s['name']}, Department: {s['dept']}\n")
            return
    print("Student not found.\n")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.\n")
