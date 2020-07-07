import discountCalculator

def main():
    amount = float(input("Please enter total bill amount:"))
    type = int(input("Please enter customer type (1. Regular 2.Primium):"))

    if (amount > 0):
        discount = discountCalculator.Discount()
        totalBill= discount.calculate(amount, type)
        discount.printResult(amount, totalBill)
    else:
        print(f"Invalid amount {amount}, should be greater than 0")

if __name__ == '__main__':
    main()