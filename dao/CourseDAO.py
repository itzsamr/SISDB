from util.DBConnUtil import create_connection
from entity.Course import Course


class CourseDAO:
    def __init__(self):
        self.conn = create_connection()

    def get_course_by_id(self, course_id):
        # Implement retrieving course by ID from the database
        pass

    def add_course(self, course):
        # Implement adding course to the database
        pass

    def update_course(self, course):
        # Implement updating course in the database
        pass

    def delete_course(self, course_id):
        # Implement deleting course from the database
        pass
