from word_count import word_count as wc

class Test_time:	
	
	def test_wc_correct(self): 
		assert wc("Let Me Down Slowly by Alec Benjamin") == 7
		assert wc("Sweater Weather") == 2
		assert wc("I Hope You're not sleeping as Tightly As You Used to Be by Aeuria") == 14
		
	def test_wc_type(self): 
		assert wc("~~ ~~ ~~") == 3
		assert wc("There are 5 people in the house. Tomorrow there will be 6!") == 12
		assert wc("5 + 10 = 22") == 0

	def test_wc_null(self): 
		assert wc("") == 0
		assert wc("   ") == 0
		assert wc("  /    ") == 1
	


