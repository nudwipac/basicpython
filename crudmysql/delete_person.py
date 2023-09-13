import pymysql
from connectdb import connectmysql as con

# update table function


def deleteperson():
    connection = con.connectdb()
    cursor = connection.cursor()

    # SQC insert data in table
    sql = """
        DELETE FROM person
        WHERE id = 4
    """

    try:
        cursor.execute(sql)
        connection.commit()
        print("DELETE data success :)")
    except pymysql.Error:
        print(pymysql.Error)


# Call addperson function
deleteperson()
