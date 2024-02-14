
empty_list = []
non_empty_list = [1, 2, 3, 4, 5]
list_of_strings = ["fred", "alice", "mary"]
list_of_lists = [[1, 2, 3], ["x", "y", "z"], [5, "ABC", None]]

my_list = []

# append to list
my_list.append("hammer")  # ["hammer"]
my_list.append("saw")     # ["hammer", "saw"]
my_list.append("chisel")  # ["hammer", "saw", "chisel"]

# clear a list
my_list = []

# iterate through a list
for my_list_item in my_list:
    print("%s" % my_list_item)

# concatenate two lists
odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]
combined_numbers = odd_numbers + even_numbers

print(repr(combined_numbers))


# insert an item at beginning of list
animals = ["cat", "dog", "zebra"]

animals.insert(0, "albatross")
print(repr(animals))


# remove an item from a list
drinks = ["coffee", "juice", "milk", "tea", "water"]

# remove "milk" from list
drinks.remove("milk")

print(repr(drinks))

# another way to remove an item from a list
drinks = ["coffee", "juice", "milk", "tea", "water"]
before_milk = drinks[0:2]
after_milk = drinks[3:]
without_milk = before_milk + after_milk

print(repr(without_milk))

