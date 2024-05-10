from util.DBConnUtil import create_connection
from entity.Student import Student
from exception.StudentNotFoundException import StudentNotFoundException


class StudentDAO:
    def __init__(self):
        self.conn = create_connection()

    def get_student_by_id(self, student_id):
        query = "SELECT * FROM Students WHERE student_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (student_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Student(*row)
        else:
            raise StudentNotFoundException(f"Student with ID {student_id} not found.")

    def add_student(self, student):
        query = "INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (?, ?, ?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                student.student_id,
                student.first_name,
                student.last_name,
                student.date_of_birth,
                student.email,
                student.phone_number,
            ),
        )
        self.conn.commit()
        cursor.close()

    def update_student(self, student):
        query = "UPDATE Students SET first_name = ?, last_name = ?, date_of_birth = ?, email = ?, phone_number = ? WHERE student_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                student.first_name,
                student.last_name,
                student.date_of_birth,
                student.email,
                student.phone_number,
                student.student_id,
            ),
        )
        self.conn.commit()
        cursor.close()

    def delete_student(self, student_id):
        query = "DELETE FROM Students WHERE student_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (student_id,))
        self.conn.commit()
        cursor.close()
