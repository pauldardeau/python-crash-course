
# using "in" is good if you just want to know if a string contains a substring
if "sun" in "lying in the sun":
    print("string contains substring")
else:
    print("string does not contain substring")

# if you need to know WHERE it occurs, use find method:
s = "lying in the sun"
pos_sun = s.find("sun")
if pos_sun > -1:
    print("substring exists at index %d" % pos_sun)
else:
    print("string does not contain substring")

