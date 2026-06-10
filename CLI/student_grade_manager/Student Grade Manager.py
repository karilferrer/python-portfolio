students = []

def add_student():
    name = input("Enter student name: ")

    try:
        grade = float(input("Enter grade: "))
    except ValueError:
        print("Invalid grade.")
        return

    students.append({
        "name": name,
        "grade": grade
    })

    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\nStudent List:")
    for student in students:
        print(f"Name: {student['name']} | Grade: {student['grade']}")

def search_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print(f"Name: {student['name']}")
            print(f"Grade: {student['grade']}")
            return

    print("Student not found.")

def calculate_average():
    if len(students) == 0:
        print("No grades available.")
        return

    total = 0

    for student in students:
        total += student["grade"]

    average = total / len(students)

    print(f"Average Grade: {average:.2f}")

while True:
    print("\n===== STUDENT GRADE MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")