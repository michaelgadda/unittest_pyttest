from palindrome import palindrome as p

class Test_time:	
	
	def test_p_correct(self): 
		assert p("racecar") == "racecar is a palindrome"
		assert p("snickers") == "snickers is not a palindrome"
		assert p("blalb") == "blalb is a palindrome"
		
	def test_p_type(self): 
		assert p("~~.~~") == "~~.~~ is a palindrome"
		assert p("90091") ==  "90091 is not a palindrome"
		assert p("123") == "123 is not a palindrome"

	def test_p_null(self): 
		assert p("") == " is a palindrome"
		assert p("  ") == "   is a palindrome"
		assert p("   ") ==  "    is not a palindrome"


