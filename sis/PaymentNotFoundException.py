class PaymentNotFoundException(Exception):
    def __init__(self, message="Payment not found."):
        self.message = message
        super().__init__(self.message)
