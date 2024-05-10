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
            try:
                student_id = input("Enter the student ID to delete: ")
                # Check if the student exists in the database
                student = student_dao.get_student_by_id(student_id)

                if student:
                    confirm = input(
                        "Are you sure you want to delete this student? (yes/no): "
                    )
                    if confirm.lower() == "yes":
                        try:
                            # Delete the student from the database
                            student_dao.delete_student(student_id)
                            print("Student deleted successfully.")
                        except Exception as e:
                            print("An error occurred while deleting the student:", e)

                    else:
                        print("Deletion canceled.")
                else:
                    print("Student not found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "4":
            # Add Course
            try:
                print("Adding a new course:")
                course_name = input("Enter course name: ")
                credits = input("Enter credits: ")
                teacher_id = input("Enter teacher ID: ")

                # Create a Course object
                new_course = Course(course_name, credits, teacher_id)

                # Add the course to the database
                course_dao.add_course(new_course)
                print("Course added successfully.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "5":
            # Update Course
            try:
                course_id = input("Enter the course ID to update: ")
                # Fetch course details from the database
                course = course_dao.get_course_by_id(course_id)

                if course:
                    print("Current details of the course:")
                    print("Course ID:", course.course_id)
                    print("Course Name:", course.course_name)
                    print("Credits:", course.credits)
                    print("Teacher ID:", course.teacher_id)

                    # Prompt user to enter updated details
                    print("\nEnter updated details:")
                    course_name = input("Enter course name: ")
                    credits = input("Enter credits: ")
                    teacher_id = input("Enter teacher ID: ")

                    # Update the course object with new details
                    course.course_name = course_name
                    course.credits = credits
                    course.teacher_id = teacher_id

                    # Update the course in the database
                    course_dao.update_course(course)
                    print("Course details updated successfully.")
                else:
                    print("Course not found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "6":
            # Delete Course
            try:
                course_id = input("Enter the course ID to delete: ")
                # Check if the course exists in the database
                course = course_dao.get_course_by_id(course_id)

                if course:
                    confirm = input(
                        "Are you sure you want to delete this course? (yes/no): "
                    )
                    if confirm.lower() == "yes":
                        # Delete the course from the database
                        course_dao.delete_course(course_id)
                        print("Course deleted successfully.")
                    else:
                        print("Deletion canceled.")
                else:
                    print("Course not found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "7":
            # Enroll Student in Course
            try:
                student_id = input("Enter the student ID: ")
                course_id = input("Enter the course ID: ")

                # Check if the student and course exist in the database
                student = student_dao.get_student_by_id(student_id)
                course = course_dao.get_course_by_id(course_id)

                if student and course:
                    # Check if the student is already enrolled in the course
                    existing_enrollments = (
                        enrollment_dao.get_enrollments_by_student_course(
                            student_id, course_id
                        )
                    )
                    if existing_enrollments:
                        raise DuplicateEnrollmentException(
                            "Student is already enrolled in this course."
                        )

                    # Create an Enrollment object
                    new_enrollment = Enrollment(student_id, course_id)

                    # Add the enrollment to the database
                    enrollment_dao.add_enrollment(new_enrollment)
                    print("Student enrolled in the course successfully.")
                else:
                    if not student:
                        raise StudentNotFoundException("Student not found.")
                    if not course:
                        raise CourseNotFoundException("Course not found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "8":
            # Record Payment
            try:
                student_id = input("Enter the student ID: ")
                amount = float(input("Enter the payment amount: "))
                payment_date = input("Enter the payment date (YYYY-MM-DD): ")

                # Check if the student exists in the database
                student = student_dao.get_student_by_id(student_id)

                if student:
                    # Create a Payment object
                    new_payment = Payment(student_id, amount, payment_date)

                    # Add the payment to the database
                    payment_dao.add_payment(new_payment)
                    print("Payment recorded successfully.")
                else:
                    raise StudentNotFoundException("Student not found.")
            except ValueError:
                print("Invalid input for amount.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "9":
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Entry point of the application
if __name__ == "__main__":
    main()
