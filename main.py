from getpass import getpass
from mysql.connector import Error, connect


try:
    with connect(
        host="localhost",
        user=input("Please enter username: "),
        password=getpass("Enter Password: "),
    ) as connection:
        print(connection)
except Error as e:
    print(f"THERE WAS AN ERROR CONNECTING TO MYSQL SERVER: {e}")
