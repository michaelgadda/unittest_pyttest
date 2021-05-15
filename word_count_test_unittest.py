import unittest 
from word_count import word_count as wc



class TestWordCount(unittest.TestCase):
    
    def test_corrrectness(self):
    	self.assertEqual(wc("Let Me Down Slowly by Alec Benjamin"), 7)
    	self.assertEqual(wc("Sweater Weather"), 3)
    	self.assertEqual(wc("I Hope You're not sleeping as Tightly As You Used to Be by Aeuria"), 14)
   
    def test_type(self):
    	self.assertEqual(wc("~~ ~~ ~~"), 3)
    	self.assertEqual(wc("There are 5 people in the house. Tomorrow there will be 6!"), 12)
    	self.assertNotEqual(wc("Sweater Weather"), 3)
    	self.assertNotEqual(wc("5 + 10 = 22"), 0)

    def test_null(self): 
    	self.assertEqual(wc(""), 0)
    	self.assertEqual(wc("   "), 0)
    	self.assertNotEqual(wc("    .     "), 0)

if __name__ == '__main__': 
	unittest.main()
