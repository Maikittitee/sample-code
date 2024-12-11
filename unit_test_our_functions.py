import unittest

import our_functions

class test_is_valid_date(unittest.TestCase):
	def test_correct_date_format(self):
		date_str = "2023-01-01"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, True)

	def test_incorrect_date_format(self):
		date_str = "03-12-2023"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)
		
	def test_not_date(self):
		date_str = "helloworld"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)

	def test_year_much(self):
		date_str = "20233-1-01"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)

	def test_none(self):
		date_str = None
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)

	def test_wrong_length(self):
		date_str = "2004-09-04-"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)

	def test_wrong_month(self):
		date_str = "2004-14-04"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)

	def test_wrong_date(self):
		date_str = "2004-02-31"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, False)

	def test_correct_date(self):
		date_str = "2003-02-28"
		res = our_functions.is_valid_date(date_str)
		self.assertEqual(res, True)
	
	
	


class test_is_valid_username(unittest.TestCase):
	def test_username_more_than_min(self):
		username_str = "myname"
		min_username_chars = 5
		res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertEqual(res, True)

	def test_username_equal_min(self):
		username_str = "myname"
		min_username_chars = 6
		res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertEqual(res, True)

	def test_username_number(self):
		username_str = 1
		min_username_chars = 6
		# res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertRaises(TypeError, our_functions.is_valid_username, username_str, min_username_chars)

	def test_username_min_char_minus(self):
		username_str = "Maiki"
		min_username_chars = -1
		# res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertRaises(ValueError, our_functions.is_valid_username, username_str, min_username_chars)

	def test_username_too_short(self):
		username_str = "Mai"
		min_username_chars = 5
		res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertEqual(res, False)

	def test_username_not_allow(self):
		username_str = "V3ry$#%^&*()"
		min_username_chars = 5
		res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertEqual(res, False)

	def test_username_start_with_number(self):
		username_str = "1hiiiiiiiiiii"
		min_username_chars = 5
		res = our_functions.is_valid_username(username_str, min_username_chars)
		self.assertEqual(res, False)


if __name__ == "__main__":
	unittest.main()