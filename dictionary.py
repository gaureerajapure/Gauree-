# Student Records Management System

students = {}

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grades = list(map(str, input("Enter grades separated by space: ").split()))
    students[student_id] = {
        "name": name,
        "age": age,
        "grades": grades
    }
    print("\nStudent added successfully.")
    display_all_students()

def display_all_students():
    print("\n--- All Student Records ---")
    if not students:
        print("No student records found.")
    else:
        for sid, info in students.items():
            print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")

def search_student():
    student_id = input("Enter student ID to search: ")
    if student_id in students:
        info = students[student_id]
        print(f"\nFound Student - ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")
    else:
        print("Student not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    if student_id in students:
        del students[student_id]
        print("Student record deleted.")
    else:
        print("Student not found.")
    display_all_students()

def update_grades():
    student_id = input("Enter student ID to update grades: ")
    if student_id in students:
        print(f"Current grades: {students[student_id]['grades']}")
        choice = input("Do you want to append a new grade or modify an existing one? (append/modify): ").lower()
        if choice == "append":
            new_grade = float(input("Enter new grade to append: "))
            students[student_id]['grades'].append(new_grade)
            print("Grade appended.")
        elif choice == "modify":
            index = int(input("Enter index of grade to modify: "))
            if 0 <= index < len(students[student_id]['grades']):
                new_grade = float(input("Enter new grade: "))
                students[student_id]['grades'][index] = new_grade
                print("Grade updated.")
            else:
                print("Invalid index.")
        else:
            print("Invalid choice.")
        print(f"Updated grades: {students[student_id]['grades']}")
    else:
        print("Student not found.")
    display_all_students()

def main():
    while True:
        print("\n--- Student Records Menu ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Delete Student by ID")
        print("5. Update Student Grades")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_grades()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()