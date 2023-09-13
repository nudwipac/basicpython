import pymysql
from connectdb import connectmysql as con
import csv

# Function อ่าน file csv และ insert into table USER


def readcsvandinserttable():
    connection = con.connectdb()
    cursor = connection.cursor()
    # read csv file
    with open('filedata/user.csv', 'r', encoding='UTF-8') as csv_file:
        # สร้าง reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        # ข้าม header
        header = next(csv_reader)

        # loop อ่าน file csv และ insert into USER table
        for row in csv_reader:
            # สร้าง SQL สำหรับ insert
            sql = "INSERT INTO users(name,email,mobile) VALUES (%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("insert success")
    connection.commit()
    connection.close()


# Call addperson function
readcsvandinserttable()
