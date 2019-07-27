import db

database_name = input('I would like to create a new database named ')
if db.connection.is_connected():
    cursor = db.connection.cursor()
    cursor.execute("CREATE DATABASE {}".format(database_name))
    print("Database {} has been created!".format(database_name))