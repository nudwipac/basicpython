# function แบบไม่รับ parameter
def hello():
    print("No parameter FUNC!")


# Call function
hello()

# function แบบรับ parameter


def area(width=0, height=0):  # default 0 ไว้เผื่อลืม input data
    total = width*height
    return total


# Call function
print("Area is", area(5, 20))
print("Area is", area(10))
print("Area is", area())
