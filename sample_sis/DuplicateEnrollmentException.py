class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Duplicate enrollment detected."):
        self.message = message
        super().__init__(self.message)
