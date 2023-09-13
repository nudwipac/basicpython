import time
num = 0
round = 1

while True:  # infinity loop
    if round < 5:
        if num == 0:
            print(round, num)
            num = 1
        elif num == 1:
            print(round, num)
            num = 0
        time.sleep(2)  # seconds
    else:
        break
    round += 1
