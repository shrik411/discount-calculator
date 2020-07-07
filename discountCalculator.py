import json
class Discount:
    def __init__(self):
        self.amount = 0
        self.customerType = 1
        self.discount = 0
        self.total = 0

    # This function calculates discount based on 
    # predefined rates
    def calculate(self, amount, type):
        try:
            # check for valid number
            self.amount = float(amount)
            self.customerType = int(type)
            self.discount = self.getDiscount(self.amount, self.customerType)
            
            totalBill = amount
            if (self.discount > 0):
                totalBill = amount - self.discount 

            return totalBill
        except (ValueError, TypeError):
            print("Invalid input!")
            raise ValueError()

    def getDiscount(self, amount, custType):
        discount = 0

        # for regular customer type
        if custType == 1:
            if (amount > 10000):
                discount += (amount - 10000) * 0.2
                amount = 10000
            if (amount <= 10000 and amount > 5000):
                discount += (amount - 5000) * 0.1      
        elif custType == 2:
            if (amount > 12000):
                discount += (amount - 12000) * 0.3
                amount = 12000
            if (amount <= 12000 and amount > 8000):
                discount += (amount - 8000) * 0.2
                amount = 8000
            if (amount <= 8000 and amount > 4000):
                discount += (amount - 4000) * 0.15
                amount = 4000
            if (amount <= 4000):
                discount += amount * 0.1
        else:
            # customer type unknown
            pass
            
        return discount

    def printResult(self, amount, total):
        discount = 0

        
        if (total != amount):
            discount = amount - total 

        out = (
            f"*****************************"
            f"*****************************\n"
            f"Total Amount: {amount:,.2f}\n"
            f"Discount: -{discount:,.2f}\n"
            f"Total Bill: {total:,.2f}\n"
        )

        print(out)