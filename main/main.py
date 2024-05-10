from dao.StudentDAO import StudentDAO
from dao.CourseDAO import CourseDAO
from dao.EnrollmentDAO import EnrollmentDAO
from dao.TeacherDAO import TeacherDAO
from dao.PaymentDAO import PaymentDAO
from exception.DuplicateEnrollmentException import DuplicateEnrollmentException
from exception.CourseNotFoundException import CourseNotFoundException
from exception.StudentNotFoundException import StudentNotFoundException
from exception.TeacherNotFoundException import TeacherNotFoundException
from exception.PaymentValidationException import PaymentValidationException
from entity.Student import Student
from entity.Course import Course
from entity.Enrollment import Enrollment
from entity.Teacher import Teacher
from entity.Payment import Payment


# Function to display the menu options
def display_menu():
    print("Student Information System (SIS) Menu:")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Add Course")
    print("5. Update Course")
    print("6. Delete Course")
    print("7. Enroll Student in Course")
    print("8. Record Payment")
    print("9. Exit")


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
        # Display the menu
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Student
            print("Adding a new student:")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")

            # Create a Student object
            new_student = Student(
                first_name, last_name, date_of_birth, email, phone_number
            )

            try:
                # Add the student to the database
                student_dao.add_student(new_student)
                print("Student added successfully.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "2":
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

        elif choice == "3":
            # Delete Student
            pass  # Implement this option

        elif choice == "4":
            # Add Course
            pass  # Implement this option

        elif choice == "5":
            # Update Course
            pass  # Implement this option

        elif choice == "6":
            # Delete Course
            pass  # Implement this option

        elif choice == "7":
            # Enroll Student in Course
            pass  # Implement this option

        elif choice == "8":
            # Record Payment
            pass  # Implement this option

        elif choice == "9":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Entry point of the application
if __name__ == "__main__":
    main()
