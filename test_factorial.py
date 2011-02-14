import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

	#def setUp(self):
	#	self.verificationErrors []
	
	#def tearDown(self):
	#	self.assertEqual([],self.verificationErrors.append(str(e))
		
	def test_empty(self):
		self.assertEqual(10,factorial.factorial(0))