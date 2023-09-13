# import ALL FUNC ใน folder module
# import module
# print(module.calculator.plus(3, 5))
# print(module.number.factorial(3))

# impot บาง function ใน folder module
from module import calculator as cal, number as num
from module import calculator, number
print(calculator.plus(4, 7))
print(number.factorial(7))

# impot พร้อมเปลี่ยนชื่อ
print(cal.plus(4, 7))
print(num.factorial(7))
