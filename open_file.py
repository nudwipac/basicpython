
# read ALL file
def read_all():
    # open file
    f = open("filedata/mydata.txt", "r", encoding="utf-8")
    print(f.read())
    # close readlines
    f.close()
    print("----------------------------------------------------------------")


# read line by line
def read_line():
    # open file
    f = open("filedata/mydata.txt", "r", encoding="utf-8")
    for i in range(5):
        print(f.readline(), end="")
    # close file
    f.close()
    print("----------------------------------------------------------------")


read_all()
read_line()
