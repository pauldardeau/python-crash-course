# string with single quotes
s = 'This is a string'
print(s)

# string with double quotes
s = "This too is a string"
print(s)

# strings can be formatted easily
name = 'Tom'
animal_type = 'cat'
s = "%s is a %s" % (name, animal_type)
print(s)

# formatting can include different types
x = 3
color1 = 'red'
color2 = 'green'
color3 = 'blue'
s = "%d common colors are %s, %s, and %s" % (x, color1, color2, color3)
print(s)

# formatting with a bool
is_working = True
s = "system is working: %s" % is_working
print(s)

# getting length of a string
s = "Hi there"
s_length = len(s)
print("The length of '%s' is %d" % (s, s_length))

# comparing strings
s1 = "Foo"
s2 = "Bar"

# are they equal?
if s1 == s2:
	print("'%s' == '%s'" % (s1, s2))

# are they not equal?
if s1 != s2:
	print("'%s' != '%s'" % (s1, s2))

# does a substring exist within a string
s1 = "The man in the moon"
substring = "man"

if substring in s1:
	print("'%s' exists in '%s'" % (substring, s1))

# finding position of substring
s1 = "The devil is in the details"
substring = "devil"
pos_devil = s1.find(substring)
print("position of '%s' within '%s' is %d" % (substring, s1, pos_devil))

# looking for something that does not exist
substring = "overview"
pos_overview = s1.find(substring)
print("position of '%s' within '%s' is %d" % (substring, s1, pos_overview))

# extracting a substring
s1 = "Take time to smell the roses"
first_four_chars = s1[0:4]
print("first 4 chars of '%s' is '%s'" % (s1, first_four_chars))

# concatenating strings
s1 = "blue"
s2 = "skies"
s3 = s1 + " " + s2
print(s3)

