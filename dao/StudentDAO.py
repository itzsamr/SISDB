from util.DBConnUtil import create_connection
from entity.Student import Student


class StudentDAO:
    def __init__(self):
        self.conn = create_connection()

    def get_student_by_id(self, student_id):
        # Implement retrieving student by ID from the database
        pass

    def add_student(self, student):
        # Implement adding student to the database
        pass

    def update_student(self, student):
        # Implement updating student in the database
        pass

    def delete_student(self, student_id):
        # Implement deleting student from the database
        pass
