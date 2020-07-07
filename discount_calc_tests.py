import unittest
from discountCalculator import Discount


class DiscountCalculatorTests(unittest.TestCase):
	def test_regular_no_discount(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(5000,1)
		self.assertEqual(5000, result)

	def test_regular_second_slab(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(10000, 1)
		self.assertEqual(9500,result)
	
	def test_regular_above_ten_k(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(15000, 1)
		self.assertEqual(13500, result)

	def test_premium_first_slab(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(4000, 2)
		self.assertEqual(3600,result)
	
	def test_premium_second_slab(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(8000, 2)
		self.assertEqual(7000,result)
	
	def test_premium_above_eight_k(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(12000, 2)
		self.assertEqual(10200, result)

	def test_premium_above_twelve_k(self):
		discount_calculator = Discount()
		result = discount_calculator.calculate(20000, 2)
		self.assertEqual(15800, result)
    
	def test_invalid_amount(self):
		discount_calculator = Discount()
		self.assertRaises(ValueError, discount_calculator.calculate, 'rrewr', 1)

    # should this fall to default customer type ? regular
	def test_invalid_cust_type(self):
		discount_calculator = Discount()
		self.assertRaises(ValueError, discount_calculator.calculate, 250, 'new')
	

if __name__ == '__main__':
    unittest.main()