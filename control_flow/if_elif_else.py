

def check_string(s):
    if s is None:
        print("string is None (not present)")
    elif len(s) == 0:
        print("string is empty")
    else:
        print("string has 1 or more characters")


s1 = None
s2 = ""
s3 = "non-empty string"

check_string(s1)
check_string(s2)
check_string(s3)

