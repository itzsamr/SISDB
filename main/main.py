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


def main():
    student_dao = StudentDAO()
    course_dao = CourseDAO()
    enrollment_dao = EnrollmentDAO()
    payment_dao = PaymentDAO()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Student
            pass  # Implement this option

        elif choice == "2":
            # Update Student
            pass  # Implement this option

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
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
