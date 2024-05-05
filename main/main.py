from util.DatabaseConnector import DatabaseConnector
from Student import Student
from Enrollment import Enrollment
from Teacher import Teacher
from Course import Course
from Payment import Payment

def main():
    # Database connection details
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'SAMAR\\MSSQLSERVER01'
    DATABASE_NAME = 'SISDB'

    # Create a database connector
    db_connector = DatabaseConnector(SERVER_NAME, DATABASE_NAME, driver=DRIVER_NAME)
    db_connector.open_connection()

    # Instantiate managers for each entity
    students_manager = Student(db_connector)
    enrollments_manager = Enrollment(db_connector)
    course_manager = Course(db_connector)
    teacher_manager = Teacher(db_connector)
    payments_manager = Payment(db_connector)

    # Example usage of each manager's methods (commented out)
    # students_manager.Add_Student(11, "John", "Doe", "1995-08-15", "john.doe@example.com", "1234567890")
    # enrollments_manager.Enroll_Course(109, 11, 201)
    # course_manager.Add_Course(211, "Advanced Database Management", "CS302", "Sarah Smith")
    # teacher_manager.Add_Teacher(311, "Sarah", "Smith", "sarah.smith@example.com")
    # payments_manager.Add_Payment(411, 11, 500, "2023-04-10")

    # More example usage...

    # Close the database connection
    db_connector.close_connection()

if __name__ == "__main__":
    main()
