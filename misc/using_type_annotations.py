

def sum_integers(x: int, y: int) -> int:
    return x + y


def print_message(s: str):
    print("%s" % s)


x: int = 3
y: int = 5

sum = sum_integers(x, y)
print("sum is %d" % sum)

msg: str = "Do you like type annotations?"
print_message(msg)
