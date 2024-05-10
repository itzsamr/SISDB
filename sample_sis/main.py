from StudentDAO import StudentDAO
from CourseDAO import CourseDAO
from EnrollmentDAO import EnrollmentDAO
from TeacherDAO import TeacherDAO
from PaymentDAO import PaymentDAO
from DuplicateEnrollmentException import DuplicateEnrollmentException
from CourseNotFoundException import CourseNotFoundException
from StudentNotFoundException import StudentNotFoundException
from TeacherNotFoundException import TeacherNotFoundException
from PaymentValidationException import PaymentValidationException
from Student import Student
from Course import Course
from Enrollment import Enrollment
from Teacher import Teacher
from Payment import Payment


# Function to display the main menu
def display_main_menu():
    print("\nStudent Information System (SIS) Menu:")
    print("1. Students")
    print("2. Courses")
    print("3. Enrollments")
    print("4. Teachers")
    print("5. Payments")
    print("6. Exit")


# Function to display the sub-menu for each entity
def display_entity_menu(entity):
    print(f"\n{entity} Menu:")
    print("1. View entire table")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("5. Back")


# Function to handle the student-related actions
def handle_student_actions(student_dao):
    while True:
        display_entity_menu("Students")
        choice = input("Enter your choice: ")

        if choice == "1":
            # View entire student table
            print("Viewing entire student table:")
            try:
                # Retrieve all students from the database
                all_students = student_dao.get_all_students()

                # Print each student's details
                for student in all_students:
                    print(f"Student ID: {student.student_id}")
                    print(f"First Name: {student.first_name}")
                    print(f"Last Name: {student.last_name}")
                    print(f"Date of Birth: {student.date_of_birth}")
                    print(f"Email: {student.email}")
                    print(f"Phone Number: {student.phone_number}")
                    print()
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "2":
            # Add Student
            print("Adding a new student:")
            student_id = input("Enter student ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")

            # Create a Student object
            new_student = Student(
                student_id, first_name, last_name, date_of_birth, email, phone_number
            )

            try:
                # Add the student to the database
                student_dao.add_student(new_student)
                print("Student added successfully.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "3":
            # Update Student
            try:
                student_id = input("Enter the student ID to update: ")
                # Fetch student details from the database
                student = student_dao.get_student_by_id(student_id)

                if student:
                    print("Current details of the student:")
                    print("Student ID:", student.student_id)
                    print("First Name:", student.first_name)
                    print("Last Name:", student.last_name)
                    print("Date of Birth:", student.date_of_birth)
                    print("Email:", student.email)
                    print("Phone Number:", student.phone_number)

                    # Prompt user to enter updated details
                    print("\nEnter updated details:")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    email = input("Enter email: ")
                    phone_number = input("Enter phone number: ")

                    # Update the student object with new details
                    student.first_name = first_name
                    student.last_name = last_name
                    student.date_of_birth = date_of_birth
                    student.email = email
                    student.phone_number = phone_number

                    # Update the student in the database
                    student_dao.update_student(student)
                    print("Student details updated successfully.")
                else:
                    print("Student not found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "4":
            # Delete student
            print("Deleting student:")
            student_id = input("Enter the student ID to delete: ")

            try:
                # Check if the student exists in the database
                student = student_dao.get_student_by_id(student_id)

                if student:
                    confirm = input(
                        "Are you sure you want to delete this student? (yes/no): "
                    )
                    if confirm.lower() == "yes":
                        # Delete the student from the database
                        student_dao.delete_student(student_id)
                        print("Student deleted successfully.")
                    else:
                        print("Deletion canceled.")
                else:
                    print("Student not found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Function to handle the course-related actions
def handle_course_actions(course_dao):
    while True:
        display_entity_menu("Courses")
        choice = input("Enter your choice: ")

        if choice == "1":
            # View entire course table
            print("Viewing entire course table:")
            # Implement this option

        elif choice == "2":
            # Add course
            print("Adding a new course:")
            # Implement this option

        elif choice == "3":
            # Update course
            print("Updating course:")
            # Implement this option

        elif choice == "4":
            # Delete course
            print("Deleting course:")
            # Implement this option

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Function to handle the enrollment-related actions
def handle_enrollment_actions(enrollment_dao):
    while True:
        display_entity_menu("Enrollments")
        choice = input("Enter your choice: ")

        if choice == "1":
            # View entire enrollment table
            print("Viewing entire enrollment table:")
            # Implement this option

        elif choice == "2":
            # Add enrollment
            print("Adding a new enrollment:")
            # Implement this option

        elif choice == "3":
            # Update enrollment
            print("Updating enrollment:")
            # Implement this option

        elif choice == "4":
            # Delete enrollment
            print("Deleting enrollment:")
            # Implement this option

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Function to handle the teacher-related actions
def handle_teacher_actions(teacher_dao):
    while True:
        display_entity_menu("Teachers")
        choice = input("Enter your choice: ")

        if choice == "1":
            # View entire teacher table
            print("Viewing entire teacher table:")
            # Implement this option

        elif choice == "2":
            # Add teacher
            print("Adding a new teacher:")
            # Implement this option

        elif choice == "3":
            # Update teacher
            print("Updating teacher:")
            # Implement this option

        elif choice == "4":
            # Delete teacher
            print("Deleting teacher:")
            # Implement this option

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Function to handle the payment-related actions
def handle_payment_actions(payment_dao):
    while True:
        display_entity_menu("Payments")
        choice = input("Enter your choice: ")

        if choice == "1":
            # View entire payment table
            print("Viewing entire payment table:")
            # Implement this option

        elif choice == "2":
            # Add payment
            print("Adding a new payment:")
            # Implement this option

        elif choice == "3":
            # Update payment
            print("Updating payment:")
            # Implement this option

        elif choice == "4":
            # Delete payment
            print("Deleting payment:")
            # Implement this option

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Main function to run the SIS application
def main():
    # Initialize DAO objects
    student_dao = StudentDAO()
    course_dao = CourseDAO()
    enrollment_dao = EnrollmentDAO()
    teacher_dao = TeacherDAO()
    payment_dao = PaymentDAO()

    # Main menu loop
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            handle_student_actions(student_dao)

        elif choice == "2":
            handle_course_actions(course_dao)

        elif choice == "3":
            handle_enrollment_actions(enrollment_dao)

        elif choice == "4":
            handle_teacher_actions(teacher_dao)

        elif choice == "5":
            handle_payment_actions(payment_dao)

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Entry point of the application
if __name__ == "__main__":
    main()
