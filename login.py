print("Login system")

# input parameters

username = input("Enter username: ")  # input จะ converse ทุกอย่างเป็น string
password = input("Enter password: ")

strA = "   test space  "
print(strA.strip())  # ตัด space ซ้าย-ขวา

if username.lower() == "admin" and password.lower() == "pass":  # case sensitive
    print("Login successful")
else:
    print("Login failed")
