from util.DBConnUtil import create_connection
from entity.Payment import Payment


class PaymentDAO:
    def __init__(self):
        self.conn = create_connection()

    def add_payment(self, payment):
        # Implement adding payment to the database
        pass

    def delete_payment(self, payment_id):
        # Implement deleting payment from the database
        pass

    def get_payments_by_student(self, student_id):
        # Implement retrieving payments by student from the database
        pass
