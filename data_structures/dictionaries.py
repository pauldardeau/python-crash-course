
# a dictionary is a data structure with key/value pairs.
# some languages refer to this kind of data structure
# as an associative array.

empty_dictionary = {}
non_empty_dictionary = {'cust1': "Bank of Toronto",
                        'cust2': "Fred's Sandwich Shop"}

my_dictionary = {}

# add key/value pairs
my_dictionary['file1.txt'] = 50000
my_dictionary['file2.txt'] = 35000
my_dictionary['file3.txt'] = 72000

num_keys = len(my_dictionary)
print("num_keys = %d" % num_keys)

keys = my_dictionary.keys()

for key in keys:
    print("key='%s', value = '%s'" % (key, my_dictionary[key]))


# remove a key/value pair
del my_dictionary['file2.txt']

num_keys = len(my_dictionary)
print("num_keys = %d after deleting one" % num_keys)

