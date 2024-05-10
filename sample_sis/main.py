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
            try:
                # Fetch all courses from the database
                all_courses = course_dao.get_all_courses()

                if all_courses:
                    # Display each course
                    for course in all_courses:
                        print("Course ID:", course.course_id)
                        print("Course Name:", course.course_name)
                        print("Credits:", course.credits)
                        print("Teacher ID:", course.teacher_id)
                        print()

                else:
                    print("No courses found.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "2":
            # Add course
            print("Adding a new course:")
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            credits = input("Enter credits: ")
            teacher_id = input("Enter teacher ID: ")

            # Create a Course object
            new_course = Course(course_id, course_name, credits, teacher_id)

            try:
                # Add the course to the database
                course_dao.add_course(new_course)
                print("Course added successfully.")
            except Exception as e:
                print("An error occurred:", e)

        elif choice == "3":
            # Update course
            print("Updating course:")
            course_id = input("Enter the course ID to update: ")

            try:
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

        elif choice == "4":
            # Delete course
            print("Deleting course:")
            course_id = input("Enter the course ID to delete: ")

            try:
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
