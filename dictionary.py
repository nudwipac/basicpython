num = {'one': 1, 'two': 2, 'three': 3}
print(num)
print(type(num))
print(num['one'])
print("---------------------------")

people = {
    1: {
        "name": "Jim",
        "age": 20,
        "city": "New York"
    },
    2: {
        "name": "Jane",
        "age": 21,
        "city": "London"
    }
}
print(people[2]["city"])

# อ่าน key ทั้งหมดจาก dictionaies
print(num.keys())
print(people.keys())
print("---------------------------")

# loop อ่านค่า key และ value ใน dic
for key, value in num.items():
    print(key, value)
print("---------------------------")

for key, value in people.items():
    print(key, value)
    for k, v in value.items():
        print(k, v, end="|")
    print("\n")
