import sqlite3 as sql
connection = sql.connect('users.db')

cursor = connection.cursor()

cursor.execute('''
    INSERT INTO users
    VALUES('CHANSE',120)
''')

connection.commit()

connection.close()