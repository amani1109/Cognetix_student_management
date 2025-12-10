import csv
import os
FILE_NAME = "students.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["StudentID", "Name", "Age", "Course"])  
def add_student():
    student_id = input("Enter Student ID: ").strip()
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    if not student_id or not name or not age or not course:
        print("All fields are required.")
        return

    if not age.isdigit():
        print("Age must be a number.")
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] == student_id:
                print("Student ID already exists!")
                return
            
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course])

    print("Student added successfully!")

def search_student():
    student_id = input("Enter Student ID to search: ").strip()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] == student_id:
                print("\n--- Student Found ---")
                print(f"ID: {row['StudentID']}")
                print(f"Name: {row['Name']}")
                print(f"Age: {row['Age']}")
                print(f"Course: {row['Course']}")
                return

    print("No student found with that ID.")


def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()

    rows = []
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["StudentID"] == student_id:
                found = True
            else:
                rows.append(row)

    if not found:
        print("No student found with that ID.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["StudentID", "Name", "Age", "Course"])
        writer.writeheader()
        writer.writerows(rows)

    print("Student deleted successfully!")

def main():
    initialize_file()

    while True:
        print("\n======= Student Management System =======")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter Option (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
