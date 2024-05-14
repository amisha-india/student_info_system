#Creating all the payment related services(CRUD) at same place (encapsulation)

from util.myDBconnection import DBConnection
class Payment_services(DBConnection):
    
    def GetStudent(self, payment_id):
        pass

    def GetPaymentAmount(self,payment_id):
        pass

    def GetPaymentDate(self,payment_id):
        pass