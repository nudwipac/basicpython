number = [-1, 0, 1, 2, 3]
print(number)
print(number[3])
print(number[-1])  # last index
print(number[1:3])  # ไม่เอา index ที่ 3
print(number[:3])  # index 0-2
print(number[1:])  # index 1-last index
print(number[:])  # ALL index
print(number[::2])  # skip ตามเลข
print(number[::-2])  # skip index จากด้านหลัง

persons = ['Ms A', 'Ms B', 'Ms C', 'Ms D', 'Ms E']
for person in persons:
    print(person)

# เพิ่มข้อมูลใน list ใช้ func append()
persons.append('Ms FF(Add)')
print(persons)

# ีupdate ข้อมูลใน list
persons[0] = 'Ms AA(Edit)'
print(persons)

# Delete
persons.remove('Ms AA(Edit)')
print(persons)
persons.pop(1)  # remove index 1
print(persons)
