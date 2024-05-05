from datetime import datetime
from Course import Course
from Enrollment import Enrollment

class Student:
    def __init__(self, StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber):
        self._StudentID = StudentID
        self._FirstName = FirstName
        self._LastName = LastName
        self._DateOfBirth = DateOfBirth
        self._Email = Email
        self._PhoneNumber = PhoneNumber
        self._enrolled_courses = []
        self._payment_history = []
        self._enrollments = []

    def __init__(self, db_connector):
        self._db_connector = db_connector

    @property
    def StudentID(self):
        return self._StudentID

    @StudentID.setter
    def StudentID(self, new_StudentID):
        if isinstance(new_StudentID, int) and new_StudentID > 0:
            self._StudentID = new_StudentID
        else:
            raise ValueError("Student ID must be a positive integer.")

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, new_FirstName):
        if isinstance(new_FirstName, str) and new_FirstName:
            self._FirstName = new_FirstName
        else:
            raise ValueError("First name must be a non-empty string.")

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_LastName):
        if isinstance(new_LastName, str) and new_LastName:
            self._LastName = new_LastName
        else:
            raise ValueError("Last name must be a non-empty string.")

    @property
    def DateOfBirth(self):
        return self._DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, new_DateOfBirth):
        self._DateOfBirth = new_DateOfBirth

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_Email):
        if isinstance(new_Email, str) and "@" in new_Email:
            self._Email = new_Email
        else:
            raise ValueError("Invalid email format.")

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, new_PhoneNumber):
        if isinstance(new_PhoneNumber, str) and new_PhoneNumber.isdigit() and len(new_PhoneNumber) == 10:
            self._PhoneNumber = new_PhoneNumber
        else:
            raise ValueError("Invalid phone number format.")

    def EnrollInCourse(self, course):
        enrollment = Enrollment(EnrollmentID=Enrollment.EnrollmentID, StudentID=self._StudentID, CourseID=course.CourseID, EnrollmentDate=Enrollment.EnrollmentDate)
        self._enrollments.append(enrollment)
        print(f"Student {self._FirstName} {self._LastName} enrolled in {course.CourseName}.")

    def UpdateStudentInfo(self, firstName, lastName, dateOfBirth, email, phoneNumber):
        self.FirstName = firstName
        self.LastName = lastName
        self.DateOfBirth = dateOfBirth
        self.Email = email
        self.PhoneNumber = phoneNumber
        print("Student information updated successfully.")

    def MakePayment(self, amount, paymentDate):
        payment_record = {"Amount": amount, "PaymentDate": paymentDate}
        self._payment_history.append(payment_record)
        print(f"Payment of {amount} made on {paymentDate} recorded successfully.")

    def DisplayStudentInfo(self):
        print(f"Student ID: {self.StudentID}")
        print(f"Name: {self.FirstName} {self.LastName}")
        print(f"Date of Birth: {self.DateOfBirth}")
        print(f"Email: {self.Email}")
        print(f"Phone Number: {self.PhoneNumber}")

    def GetEnrolledCourses(self):
        return self._enrolled_courses

    def GetPaymentHistory(self):
        return self._payment_history

    @property
    def Enrollments(self):
        return self._enrollments

    @Enrollments.setter
    def Enrollments(self, new_enrollments):
        if isinstance(new_enrollments, list) and all(isinstance(enrollment, Enrollment) for enrollment in new_enrollments):
            self._enrollments = new_enrollments
        else:
            raise ValueError("Invalid list of enrollments.")

    def Add_Student(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (student_id, first_name, last_name, date_of_birth, email, phone_number)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("STUDENT DETAILS ADDED successfully.")

        except Exception as e:
            print(f"Error adding student details: {e}")

        finally:
            self._db_connector.close_connection()
