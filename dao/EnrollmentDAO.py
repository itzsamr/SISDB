from util.DBConnUtil import create_connection
from entity.Enrollment import Enrollment


class EnrollmentDAO:
    def __init__(self):
        self.conn = create_connection()

    def add_enrollment(self, enrollment):
        # Implement adding enrollment to the database
        pass

    def delete_enrollment(self, enrollment_id):
        # Implement deleting enrollment from the database
        pass

    def get_enrollments_by_student(self, student_id):
        # Implement retrieving enrollments by student from the database
        pass

    def get_enrollments_by_course(self, course_id):
        # Implement retrieving enrollments by course from the database
        pass
