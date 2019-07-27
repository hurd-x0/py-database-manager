import mysql.connector
import config
import os

print("Database Helper, created with ♥ by littleflower ...")

connection = mysql.connector.connect(
    host = "localhost",
    user = config.username,
    passwd = config.password,
    auth_plugin='mysql_native_password',
)