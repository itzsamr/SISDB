from DBConnUtil import create_connection
from Course import Course
from Student import Student
from Teacher import Teacher
from CourseNotFoundException import CourseNotFoundException
from datetime import datetime


class SISDAO:
    def __init__(self):
        self.conn = create_connection()

    def EnrollStudentInCourse(
        self, enrollment_id, student_id, course_id, enrollment_date
    ):
        query = "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                enrollment_id,
                student_id,
                course_id,
                enrollment_date,
            ),
        )
        self.conn.commit()
        cursor.close()

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

    def AssignTeacherToCourse(self, teacher: Teacher, course: Course):
        query = "UPDATE Courses SET teacher_id = ? WHERE course_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (teacher.teacher_id, course.course_id))
        self.conn.commit()
        cursor.close()

    def RecordPayment(
        self, payment_id: int, student: Student, amount: float, paymentDate: datetime
    ):
        query = """
            INSERT INTO Payments (payment_id, student_id, amount, payment_date) 
            VALUES (?, ?, ?, ?)
        """
        cursor = self.conn.cursor()

        cursor.execute(query, (payment_id, student.student_id, amount, paymentDate))
        self.conn.commit()
        cursor.close()

    def GenerateEnrollmentReport(self, course: Course):
        query = """
            SELECT Students.student_id, Students.first_name, Students.last_name 
            FROM Students 
            INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id 
            WHERE Enrollments.course_id = ?
        """
        cursor = self.conn.cursor()
        cursor.execute(query, (course.course_id,))
        rows = cursor.fetchall()
        cursor.close()

        enrollment_report = []
        for row in rows:
            student_id, first_name, last_name = row
            student_name = f"{first_name} {last_name}"
            enrollment_report.append(
                {"student_id": student_id, "student_name": student_name}
            )

        return enrollment_report

    def GeneratePaymentReport(self, student: Student):
        query = "SELECT amount, payment_date FROM Payments WHERE student_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (student.student_id,))
        rows = cursor.fetchall()
        cursor.close()

        payment_report = []
        for row in rows:
            amount, payment_date = row
            payment_report.append({"amount": amount, "payment_date": payment_date})

        return payment_report

    def CalculateCourseStatistics(self, course: Course):
        query_enrollments = "SELECT COUNT(*) FROM Enrollments WHERE course_id = ?"
        query_total_payments = "SELECT SUM(amount) FROM Payments INNER JOIN Enrollments ON Payments.student_id = Enrollments.student_id WHERE Enrollments.course_id = ?"

        cursor = self.conn.cursor()

        cursor.execute(query_enrollments, (course.course_id,))
        enrollments = cursor.fetchone()[0]

        cursor.execute(query_total_payments, (course.course_id,))
        total_payments = cursor.fetchone()[0]

        cursor.close()

        return {"enrollments": enrollments, "total_payments": total_payments}
