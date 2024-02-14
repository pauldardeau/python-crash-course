
# a list is essentially a dynamic array

trees = ["elm", "maple", "oak", "pine"]

for tree in trees:
    print("%s" % tree)

num_trees = len(trees)

print("%d trees in tuple" % num_trees)

odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]
combined_numbers = odd_numbers + even_numbers

print(repr(combined_numbers))

drinks = ["coffee", "juice", "milk", "tea", "water"]

# remove "milk"
drinks.remove("milk")

print(repr(drinks))

