# สร้างตัวแปร
a = 10
b = 3.14
c = "Hello"

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print("----------------------", "\n")

# ข้อมูลคนละ type กันบวกได้
print(a + b)

# converse type
print(int(b))
print(float(a))
print("----------------------", "\n")

# boolean
status = True
msg = False
print(status)
print(msg)
print("----------------------", "\n")

# True = 1 / False = 0
print(status == 1)
print(msg == 0)
print("----------------------", "\n")

# แสดงผลตัวร่วมกับข้อความ
price = 200.56
price2 = 30.45
qty = 5
print("ราคาสินค้า", price, "บาท", "จำนวน", qty)
print("ราคาสินค้า %.1f บาท จำนวน %d ชิ้น" % (price, qty))
print("ราคาสินค้า %.1f บาท จำนวน %f ชิ้น" % (price, price2))
print(f"ราคาสินค้า {price:.3f} บาท จำนวน {qty} ชิ้น")
print("----------------------", "\n")
