# python is interpreted. this means that a piece of code is not
# completely evaluated until execution reaches it.


def bad_func():
	# let's try to call a module function that we haven't imported

    # the following statement crashes due to error:
    # NameError: global name 'json' is not defined
    json_obj = json.loads("['a', 'b', 'c']")


# calling bad_func will crash with an error, but just having it
# in our program does not produce any error
# bad_func()

x = 3
print(x)

