class EnrollmentNotFoundException(Exception):
    def __init__(self, message="Enrollment not found."):
        self.message = message
        super().__init__(self.message)
