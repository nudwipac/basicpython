import pymysql
from connectdb import connectmysql as con
from tabulate import tabulate

# Create table function


def readperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC select
    sql = """
        SELECT * FROM person
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("insert data success :)")
        # ดึงข้อมูล
        # result = cursor.fetchall()
        # for row in result:
        #    print(row['fullname'], row['email'], row['age'])
        # Display data
        header = {'id': 'ID', 'fullname': 'Fullname',
                  'email': 'Email', 'age': 'Age'}
        print(tabulate(cursor, headers=header, tablefmt="pretty"))
    except pymysql.Error:
        print(pymysql.Error)


# Call function
readperson()
