from Student import Student
from Teacher import Teacher
from Course import Course
from Payment import Payment
from Enrollment import Enrollment
from datetime import datetime
from exception import StudentNotFoundException, CourseNotFoundException, TeacherNotFoundException

class SIS:
    def __init__(self):
        self._enrollments = []
        self._teachers_assigned_courses = []
        self._payments = []
        self.students = []
        self.courses = []
        self.teachers = []
        self.enrollments = []
        self.payments = []

    def EnrollStudentInCourse(self, student, course):
        enrollment = {"student": student, "course": course}
        self._enrollments.append(enrollment)
        print(f"Student {student.FirstName} enrolled in {course.CourseName}.")

    def AssignTeacherToCourse(self, teacher, course):
        teacher_assignment = {"teacher": teacher, "course": course}
        self._teachers_assigned_courses.append(teacher_assignment)
        print(f"Teacher {teacher.FirstName} assigned to {course.CourseName}.")

    def RecordPayment(self, paymentid, studentid, amount, paymentDate):
        payment = Payment(paymentid, studentid, amount, paymentDate)
        self._payments.append(payment)
        print(f"Payment of {amount} recorded successfully.")

    def GenerateEnrollmentReport(self, course):
        enrolled_students = [enrollment["student"] for enrollment in self._enrollments if enrollment["course"] == course]
        print(f"Enrollment Report for {course.CourseName}:")
        for student in enrolled_students:
            print(f"- {student.FirstName} {student.LastName}")

    def GeneratePaymentReport(self, student):
        student_payments = [payment for payment in self._payments if payment.StudentID == student.StudentID]
        print(f"Payment Report for {student.FirstName} {student.LastName}:")
        for payment in student_payments:
            print(f"- Amount: {payment.amount}, Date: {payment.paymentDate}")

    def CalculateCourseStatistics(self, course):
        enrollments_count = len([enrollment for enrollment in self._enrollments if enrollment["course"] == course])
        total_payments = sum([payment.Amount for payment in self._payments if payment.CourseID == course.CourseID])
        print(f"Course Statistics for {course.CourseName}:")
        print(f"- Enrollments: {enrollments_count}")
        print(f"- Total Payments: {total_payments}")

    def AddEnrollment(self, student, course, enrollment_date):
        if student not in self.students:
            raise StudentNotFoundException("Student not found in the system.")
        if course not in self.courses:
            raise CourseNotFoundException("Course not found in the system.")
        enrollment = Enrollment(len(self.enrollments) + 1, student, course, enrollment_date)
        student.Enrollments.append(enrollment)
        course.Enrollments.append(enrollment)

        self.enrollments.append(enrollment)

    def AssignCourseToTeacher(self, course, teacher):
        if course not in self.courses:
            raise CourseNotFoundException("Course not found in the system.")
        if teacher not in self.teachers:
            raise TeacherNotFoundException("Teacher not found in the system.")

        teacher.AssignedCourses.append(course)

    def AddPayment(self, student, amount, payment_date):
        if student not in self.students:
            raise StudentNotFoundException("Student not found in the system.")

        payment = Payment(PaymentID=len(self.payments) + 1, StudentID=student.StudentID, Amount=amount,
                          PaymentDate=payment_date)

        self.payments.append(payment)

        print(f"Payment of {amount} made by {student.FirstName} {student.LastName} on {payment_date}.")

    def GetEnrollmentsForStudent(self, student):
        if student not in self.students:
            raise StudentNotFoundException("Student not found in the system.")

        student_enrollments = [enrollment for enrollment in self.enrollments if enrollment.StudentID == student.StudentID]
        return student_enrollments

    def GetCoursesForTeacher(self, teacher):
        if teacher not in self.teachers:
            raise TeacherNotFoundException("Teacher not found in the system.")

        teacher_courses = [course for course in teacher.AssignedCourses]
        return teacher_courses

sis = SIS()
student = Student(StudentID=1, FirstName="Aniket", LastName="Biyani", DateOfBirth=datetime(2002, 3, 8),
                  Email="aniket.biyani@gmail.com", PhoneNumber="1234567890")
sis.students.append(student)
teacher = Teacher(101, "Karthika","Thangiraj","karthikamca@gmail.com")
sis.teachers.append(teacher)
course = Course(101, "Python", "101", "Professor Karthika")
sis.courses.append(course)

sis.AddEnrollment(student, course, datetime.now())

sis.AssignCourseToTeacher(course, teacher)
enrollments_for_student = sis.GetEnrollmentsForStudent(student)
print(f"Enrollments for {student.FirstName} {student.LastName}:")
for enrollment in enrollments_for_student:
    print(f"- Course: {enrollment.Course.CourseName}, Enrollment Date: {enrollment.EnrollmentDate}")

courses_for_teacher = sis.GetCoursesForTeacher(teacher)
print(f"Courses assigned to {teacher.FirstName}:")
for course in courses_for_teacher:
    print(f"- {course.CourseName}")
