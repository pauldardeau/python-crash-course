
def divide_by_zero(dividend):
    x = dividend / 0  # raises ZeroDivisionError


def read_non_existent_file():
    with open("/abc/def/ghi/jkl/mno.pqr", "r") as f:  # raises IOError
        f.read() 


def access_non_existing_element():
    l = []
    m = l[5]  # raises IndexError


def call_method_on_none():
    s = None
    s.endswith(".txt")  # raises AttributeError


try:
    divide_by_zero(5)
except ZeroDivisionError as e:
    print("ZeroDivisionError exception caught")
    # can raise it again by uncommenting following line
    #raise e

try:
    read_non_existent_file()
except IOError:
    print("IOError caught")
    # can raise it again by uncommenting following line
    #raise


try:
    access_non_existing_element()
except IndexError:
    print("IndexError caught")
    # can raise it again by uncommenting following line
    #raise

try:
    call_method_on_none()
except AttributeError:
    print("AttributeError caught")
    # can raise it again by uncommenting following line
    #raise


