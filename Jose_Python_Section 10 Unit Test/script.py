"""This is a Unit Test script"""
import unittest
import cap
class TestCap(unittest.TestCase): 
	"""Unit Test class"""
	def test_one_word(self):# All test methods must start with test_xxx or it will not execute
		"""Single word test"""
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,"Python")
	def test_muti_word(self):
		"""Multi word test"""
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result,text)
if __name__ == '__main__':
	"""Run main function"""
	unittest.main()
