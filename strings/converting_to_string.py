
int_value = 5

# the following lines all produce "5"
str_value = "%d" % int_value
print("%s" % str_value)

str_value = str(int_value)
print("%s" % str_value)


float_value = 3.14

# the following lines all produce "3.14"

str_value = "%.2f" % float_value
print("%s" % str_value)

str_value = str(float_value)
print("%s" % str_value)

