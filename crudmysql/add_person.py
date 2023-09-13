import pymysql
from connectdb import connectmysql as con

# Create table function


def addperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC insert data in table
    sql = """
        INSERT INTO person(fullname, email, age)
        VALUES('Gabi','gabi@gmail.com',25)
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("insert data success :)")
    except pymysql.Error:
        print(pymysql.Error)


# Call addperson function
addperson()
