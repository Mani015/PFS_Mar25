

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def payment_money(self,amount):
        pass



class Credit_Card(Payment):

    def payment_money(self, amount : int):

        return f"Payment debit from your credit card rupees : {amount}"


class IOU(Payment):

    def payment_money(self, amount: float):
        return f"Payment debit from your IOU card rupees : {amount}"


class Phone_pay(Payment):

    def payment_money(self,amount: int):
        return f"Payment debit fro phone pay rupees : {amount}"



def debit(payment : Payment):

    return payment.payment_money(3000)

ob1 = Credit_Card()
ob2 = IOU()
ob3 = Phone_pay()

# print(debit(ob1))
# Payment debit from your credit card rupees : 3000

print(debit(ob2))
# Payment debit from your IOU card rupees : 3000



