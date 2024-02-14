# in python, whitespace is very important!!

# scoping blocks of code is done with indentation

# standard in python community is 4 SPACES (never use TABs)

email_address = "tom@gmail.com"

if "@" in email_address and email_address.endswith(".com"):
	print("'%s' looks like it might be a valid email address" % email_address)
else:
	print("'%s' does not appear to be a valid email address" % email_address)


def my_function():
	print("my_function line 1")
	print("my_function line 2")

# if you add 4 leading spaces to following line it will be part of my_function
print("this line is NOT part of my_function because it's not indented")

my_function()


# let's do something that WILL cause an error
try:
	z = 5 / 0
except Exception as e:
	# here is where we put code to handle division by 0 error
	print("division by 0 is not allowed")
	print("division by 0 is not defined")
print("maybe check whether divisor is 0 before using it in division")


# let's do something that DOES NOT cause an error
try:
	z = 5 / 2
except Exception as e:
	# here is where we put code to handle division by 0 error
	print("division by 0 is not allowed")
	print("division by 0 is not defined")
print("maybe check whether divisor is 0 before using it in division")
