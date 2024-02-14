# here is how you construct a list
colors = ['red', 'green', 'blue']

if len(colors) > 0:
	print("we have some colors")
else:
	print("we don't have any colors")

empty_list = []

# start with an empty list
common_words = []

# append to the list
common_words.append("the")
common_words.append("and")
common_words.append("there")

# see if list contains a specific element
if "is" in common_words:
	print("'is' is contained in common_words")
else:
	print("'is' is NOT contained in common_words")

if "and" in common_words:
	print("'and' is contained in common_words")
else:
	print("'and' is NOT contained in common_words")

animals = ["dog", "cat", "mouse", "giraffe"]

print("animal names contained in animals list:")
for animal in animals:
	print(animal)
