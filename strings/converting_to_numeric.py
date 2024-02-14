
age_as_string = "21"

age_as_int = int(age_as_string)
print("age = %d" % age_as_int)

maybe_not_valid_int = "xyz"
try:
    value_as_int = int(maybe_not_valid_int)
except ValueError:
    print("string cannot be converted to an integer")

pi_as_string = "3.14"

pi_as_float = float(pi_as_string)
print("pi value = %f" % pi_as_float)

maybe_not_valid_float = "s5Hx@n!"
try:
    value_as_float = float(maybe_not_valid_float)
except ValueError:
    print("string cannot be converted to a float")

