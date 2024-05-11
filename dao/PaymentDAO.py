from util.DBConnUtil import create_connection
from entity.Payment import Payment
from exception.PaymentNotFoundException import PaymentNotFoundException


class PaymentDAO:
    def __init__(self):
        self.conn = create_connection()

    def add_payment(self, payment):
        query = "INSERT INTO Payments (payment_id, student_id, amount, payment_date) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                payment.payment_id,
                payment.student_id,
                payment.amount,
                payment.payment_date,
            ),
        )
        self.conn.commit()
        cursor.close()

    def delete_payment(self, payment_id):
        query = "DELETE FROM Payments WHERE payment_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (payment_id,))
        self.conn.commit()
        cursor.close()

    def get_payments_by_student(self, student_id):
        query = "SELECT * FROM Payments WHERE student_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (student_id,))
        rows = cursor.fetchall()
        cursor.close()
        payments = []
        for row in rows:
            payments.append(Payment(*row))
        return payments

    def get_all_payments(self):
        try:
            query = "SELECT * FROM Payments"
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()

            # Initialize a list to store Payment objects
            all_payments = []

            # Iterate over the rows and create Payment objects
            for row in rows:
                payment = Payment(*row)
                all_payments.append(payment)

            return all_payments

        except Exception as e:
            # Handle any exceptions that may occur during the database operation
            print("An error occurred:", e)
            return []

    def get_payment_by_id(self, payment_id):
        query = "SELECT * FROM Payments WHERE payment_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (payment_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Payment(*row)
        else:
            return None

    def update_payment(self, payment):
        query = "UPDATE Payments SET student_id = ?, amount = ?, payment_date = ? WHERE payment_id = ?"
        cursor = self.conn.cursor()
        cursor.execute(
            query,
            (
                payment.student_id,
                payment.amount,
                payment.payment_date,
                payment.payment_id,
            ),
        )
        self.conn.commit()
        cursor.close()
