# many people assume that python is not strongly typed because type
# declarations are not required. this is not true. it is strongly
# typed as we demonstrate below.


def do_string_stuff(x):
    if type(x) is str:
        y = x[2]
        is_txt = x.endswith(".txt")
        # all good!
    else:
    	# this ordinarily wouldn't end well, but we'll address it
    	try:
    		y = x[2]
    		is_txt = x.endswith(".txt")
    	except Exception as e:
    		# an exception was raised because python is strongly typed
    		print("You passed a non-string (%s) to function that requires a string" % str(type(x)))


x = 5
do_string_stuff(x)

x = "report.txt"
do_string_stuff(x)