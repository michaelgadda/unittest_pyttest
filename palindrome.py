def palindrome(word):
	

	left_side_word = word[:int(len(word)/2)]
	right_side_word = word[int(len(word)/2):]

	for idx in range(len(left_side_word)): 
		if left_side_word[idx] == right_side_word[len(right_side_word)-1-idx]:
			 continue
		else:
			print(f"{word} is not a palindrome")
			return f"{word} is not a palindrome"
	print(f"{word} is a palindrome")		
	return f"{word} is a palindrome"

	