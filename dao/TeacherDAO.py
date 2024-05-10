from util.DBConnUtil import create_connection
from entity.Teacher import Teacher
from exception.TeacherNotFoundException import TeacherNotFoundException


class TeacherDAO:
    def __init__(self):
        self.conn = create_connection()

    def get_teacher_by_id(self, teacher_id):
        query = "SELECT * FROM Teacher WHERE teacher_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (teacher_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Teacher(*row)
        else:
            raise TeacherNotFoundException(f"Teacher with ID {teacher_id} not found.")

    def add_teacher(self, teacher):
        query = "INSERT INTO Teacher (teacher_id, first_name, last_name, email) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (teacher.teacher_id, teacher.first_name, teacher.last_name, teacher.email),
        )
        self.conn.commit()
        cursor.close()

    def update_teacher(self, teacher):
        query = "UPDATE Teacher SET first_name = ?, last_name = ?, email = ? WHERE teacher_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (teacher.first_name, teacher.last_name, teacher.email, teacher.teacher_id),
        )
        self.conn.commit()
        cursor.close()

    def delete_teacher(self, teacher_id):
        query = "DELETE FROM Teacher WHERE teacher_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (teacher_id,))
        self.conn.commit()
        cursor.close()
