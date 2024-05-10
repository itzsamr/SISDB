from util.DBConnUtil import create_connection
from entity.Teacher import Teacher


class TeacherDAO:
    def __init__(self):
        self.conn = create_connection()

    def get_teacher_by_id(self, teacher_id):
        # Implement retrieving teacher by ID from the database
        pass

    def add_teacher(self, teacher):
        # Implement adding teacher to the database
        pass

    def update_teacher(self, teacher):
        # Implement updating teacher in the database
        pass

    def delete_teacher(self, teacher_id):
        # Implement deleting teacher from the database
        pass
