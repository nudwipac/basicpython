import pymysql
from connectdb import connectmysql as con

# update table function


def updateperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC insert data in table
    sql = """
        UPDATE person SET fullname='James เรืองศักดิ์'
        WHERE id = 3
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("Update data success :)")
    except pymysql.Error:
        print(pymysql.Error)


# Call addperson function
updateperson()
