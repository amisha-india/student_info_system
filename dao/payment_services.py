from util import *
from myexception.exception_handeling import PaymentValidationException
from entity.payment import Payment


class Payment_management:
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    # Getting the payment amount
    def get_payment_amount(self):
        stmt = self.conn.cursor()

        try:
            student_id = int(input("Enter the student id:"))
            stmt.execute(
                "select amount from Payments  inner join students on Payments.student_id=students.student_id where students.student_id=?;",
                (student_id),
            )
            print(stmt.fetchall())
        except Exception as e:
            raise PaymentValidationException(
                "Error: In retrieve the data".format(str(e))
            )

    # Getting the payment data
    def get_payment_date(self):
        stmt = self.conn.cursor()

        try:
            payment_id = int(input("Enter the payment id:"))
            stmt.execute(
                "select payment_date from Payments where payment_id=?;", (payment_id)
            )
            print(stmt.fetchall())
        except Exception as e:
            raise PaymentValidationException(
                "Error: In retrieving the data".format(str(e))
            )

    # Getting student based on payment id
    def get_student(self):
        stmt = self.conn.cursor()

        try:
            payment_id = int(input("Enter the payment id:"))
            stmt.execute(
                "select * from Payments p inner join students s on p.student_id=s.student_id where payment_id=?;",
                (payment_id),
            )
            print(stmt.fetchall())
        except Exception as e:
            raise PaymentValidationException("Error: In retrieving data".format(str(e)))
