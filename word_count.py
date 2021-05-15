
# As defined by google dictionary a word is : a single distinct meaningful element of speech or writing, used with others (or sometimes alone) to form a sentence and typically shown with a space on either side when written or printed.
#I will be counting symbols and numbers as words

def word_count(words):
	

	word_list = words.split()
	print(f"{words} has {len(word_list)} words.")
	return len(word_list)

