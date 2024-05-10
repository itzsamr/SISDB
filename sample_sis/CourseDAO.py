from DBConnUtil import create_connection
from Course import Course
from CourseNotFoundException import CourseNotFoundException


class CourseDAO:
    def __init__(self):
        self.conn = create_connection()

    def get_course_by_id(self, course_id):
        query = "SELECT * FROM Courses WHERE course_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (course_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Course(*row)
        else:
            raise CourseNotFoundException(f"Course with ID {course_id} not found.")

    def add_course(self, course):
        query = "INSERT INTO Courses (course_id, course_name, credits, teacher_id) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (course.course_id, course.course_name, course.credits, course.teacher_id),
        )
        self.conn.commit()
        cursor.close()

    def update_course(self, course):
        query = "UPDATE Courses SET course_name = ?, credits = ?, teacher_id = ? WHERE course_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (course.course_name, course.credits, course.teacher_id, course.course_id),
        )
        self.conn.commit()
        cursor.close()

    def delete_course(self, course_id):
        query = "DELETE FROM Courses WHERE course_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (course_id,))
        self.conn.commit()
        cursor.close()
