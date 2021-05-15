import unittest 
from palindrome import palindrome as p



class TestPalindrome(unittest.TestCase):
    
    def test_corrrectness(self):
    	self.assertEqual(p("racecar"), "racecar is a palindrome")
    	self.assertEqual(p("snickers"), "snickers is not a palindrome")
    	self.assertEqual(p("blalb"), "blalb is a palindrome")
   
    def test_type(self):
    	self.assertEqual(p("~~.~~"), "~~.~~ is a palindrome")
    	self.assertEqual(p("90091"), "90091 is a palindrome")
    	self.assertNotEqual(p("123"), "123 is a palindrome")
    	self.assertNotEqual(p("?!++?!"), "?!++?! is not a palindrome")

    def test_null(self): 
    	self.assertEqual(p(""), " is a palindrome")
    	self.assertEqual(p("  "), "   is a palindrome")
    	self.assertNotEqual(p("   "), "    is not a palindrome")

if __name__ == '__main__': 
	unittest.main()
