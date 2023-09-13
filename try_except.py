try:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    print(f"{num1}/{num2}={num1/num2}")
except ValueError:
    print("Pls enter a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception:
    print("Something went wrong")
