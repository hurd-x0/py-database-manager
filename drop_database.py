import db

database_name = input('I would like to drop a database named ')
if db.connection.is_connected():
    cursor = db.connection.cursor()
    cursor.execute("DROP DATABASE {}".format(database_name))
    print("Database {} has been dropped!".format(database_name))