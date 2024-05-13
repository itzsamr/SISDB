from DBConnUtil import create_connection
from Student import Student
from StudentNotFoundException import StudentNotFoundException


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

    def get_all_students(self):
        query = "SELECT * FROM Students"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        # Create Student objects for each row and return a list of them
        all_students = []
        for row in rows:
            student = Student(*row)
            all_students.append(student)

        return all_students
