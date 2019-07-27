import db
import sys

if db.connection.is_connected():
    for database_name in sys.argv[1:len(sys.argv)]:
        cursor = db.connection.cursor()
        cursor.execute("CREATE DATABASE {}".format(database_name))
        print(" > Database {} has been created!".format(database_name))