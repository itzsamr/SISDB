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
