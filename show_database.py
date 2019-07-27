import db

print('Here are the list of the databases\' name available on your system :')
if db.connection.is_connected():
    cursor = db.connection.cursor()
    cursor.execute("SHOW DATABASES")
    results = cursor.fetchall()
    for result in results:
        database_name = result[0]
        print(" > {}".format(database_name))