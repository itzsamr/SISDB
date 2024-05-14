from util.DBConnUtil import create_connection
from entity.Course import Course
from exception.CourseNotFoundException import CourseNotFoundException


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

    def get_all_courses(self):
        query = "SELECT * FROM Courses"
        cursor = self.conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        all_courses = []
        for row in rows:
            course = Course(*row)
            all_courses.append(course)

        return all_courses

    def get_course_by_name(self, course_name):
        # Assuming you're using some database library to interact with the database
        # Here's how you can modify the method to use parameterized queries
        cursor = self.conn.cursor()

        # Execute a parameterized query to select the course by name
        query = "SELECT * FROM courses WHERE course_name = ?"
        cursor.execute(query, (course_name,))  # Pass course_name as a tuple

        # Fetch the course record
        course_record = cursor.fetchone()

        # Check if the course exists in the database
        if course_record:
            # Extract course details from the database record
            course_id, course_name, credits, teacher_id = course_record
            # Create and return a Course object with the retrieved details
            return Course(course_id, course_name, credits, teacher_id)
        else:
            # Return None if the course is not found
            return None
