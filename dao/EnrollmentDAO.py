from dao.CourseDAO import CourseDAO
from util.DBConnUtil import create_connection
from entity.Enrollment import Enrollment
from exception.EnrollmentNotFoundException import EnrollmentNotFoundException


class EnrollmentDAO:
    def __init__(self):
        self.conn = create_connection()

    def add_enrollment(self, enrollment):
        query = "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                enrollment.enrollment_id,
                enrollment.student_id,
                enrollment.course_id,
                enrollment.enrollment_date,
            ),
        )
        self.conn.commit()
        cursor.close()

    def delete_enrollment(self, enrollment_id):
        query = "DELETE FROM Enrollments WHERE enrollment_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (enrollment_id,))
        self.conn.commit()
        cursor.close()

    def get_enrollments_by_student(self, student_id):
        query = "SELECT * FROM Enrollments WHERE student_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (student_id,))
        rows = cursor.fetchall()
        cursor.close()
        enrollments = []
        for row in rows:
            enrollments.append(Enrollment(*row))
        return enrollments

    def get_enrollments_by_course(self, course_id):
        query = "SELECT * FROM Enrollments WHERE course_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (course_id,))
        rows = cursor.fetchall()
        cursor.close()
        enrollments = []
        for row in rows:
            enrollments.append(Enrollment(*row))
        return enrollments

    def get_all_enrollments(self):
        try:
            # SQL query to select all enrollments
            query = "SELECT * FROM Enrollments"

            # Create a cursor object to execute the query
            cursor = self.conn.cursor()

            # Execute the query
            cursor.execute(query)

            # Fetch all rows from the result set
            rows = cursor.fetchall()

            # Close the cursor
            cursor.close()

            # Initialize a list to store Enrollment objects
            all_enrollments = []

            # Iterate over the rows and create Enrollment objects
            for row in rows:
                enrollment = Enrollment(*row)
                all_enrollments.append(enrollment)

            return all_enrollments

        except Exception as e:
            # Handle any exceptions that may occur during the database operation
            print("An error occurred:", e)
            return []

    def get_enrollment_by_id(self, enrollment_id):
        query = "SELECT * FROM Enrollments WHERE enrollment_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (enrollment_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Enrollment(*row)
        else:
            raise EnrollmentNotFoundException(
                f"Enrollment with ID {enrollment_id} not found."
            )

    def update_enrollment(self, enrollment):
        query = "UPDATE Enrollments SET student_id = ?, course_id = ?, enrollment_date = ? WHERE enrollment_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                enrollment.student_id,
                enrollment.course_id,
                enrollment.enrollment_date,
                enrollment.enrollment_id,
            ),
        )
        self.conn.commit()
        cursor.close()

    def generate_enrollment_report(course_name):
        # Initialize EnrollmentDAO and CourseDAO objects
        enrollment_dao = EnrollmentDAO()
        course_dao = CourseDAO()

        try:
            # Get course ID for the given course name
            course = course_dao.get_course_by_name(course_name)

            if course:
                # Retrieve enrollment records for the specified course
                enrollments = enrollment_dao.get_enrollments_by_course(course.course_id)

                if enrollments:
                    # Generate the report header
                    report = f"Enrollment Report for Course: {course_name}\n\n"
                    report += "{:<15} {:<20} {:<15}\n".format(
                        "Student ID", "Student Name", "Enrollment Date"
                    )
                    report += "-" * 50 + "\n"

                    # Add enrollment details to the report
                    for enrollment in enrollments:
                        student_name = f"{enrollment.student.first_name} {enrollment.student.last_name}"
                        report += "{:<15} {:<20} {:<15}\n".format(
                            enrollment.student_id,
                            student_name,
                            enrollment.enrollment_date,
                        )

                    # Display or save the report
                    print(report)  # Displaying the report to the console
                    # You can also save the report to a file if needed

                else:
                    print(f"No enrollments found for course: {course_name}")

            else:
                print(f"Course '{course_name}' not found.")

        except Exception as e:
            print("An error occurred:", e)
