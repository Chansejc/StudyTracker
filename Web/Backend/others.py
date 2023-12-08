from ST_time import get_stime_iter
from ST_time import sesh_length
import time as time
import sqlite3 as sql
from Utils import list_to_entry
import typing

#Added a method for getting the most recent session_length 
#for users in the database in order to display the information
#in the UI

def open_connection(db : str): 
    connection = sql.connect(f'{db}.db')
    cursor = connection.cursor()
    return (cursor, connection)


def close_commit_connection(connection, query=()):
    connection.commit()
    connection.close()
    if query:
        print(f'This is the result of a query: {query}')


def get_time_string():
    import time
    t = time.ctime()
    t = t[11:19]
    return t

def getUserEntryCount(username, database, table):
    cursor, connection = open_connection(database)
    cursor.execute('''
                SELECT count(*) 
                FROM {0} 
                WHERE username='{1}'
                   '''.format(table, username))
    query = cursor.fetchone()
    close_commit_connection(connection, query)
    return int(query[0])


class RecordsDatabase:
    def __init__(self, db, tables):
        self.self = self
        self.db = db
        self.tables = tables

    def get_entries(self, table):
        try:
            if table in self.tables:
                cursor, connection = open_connection(self.db)
                cursor.execute('''
                    SELECT * FROM {}
                    '''.format(table))
                query = cursor.fetchall()
                close_commit_connection(connection, query)
                return query
        except sql.OperationalError:
            print("Query Unsuccessful. Table not in Database.\
                \nOr table not in current Directory.""")
            return

    def send_start_entry(self, table:str, listOfValues: list) -> None:
        t = get_time_string()
        entry_Number = getUserEntryCount(listOfValues[0], self.db, table) + 1
        values = list_to_entry(listOfValues)
        #print(values)
        if table in self.tables:
            cursor, connection = open_connection(self.db)
            cursor.execute('''
                        INSERT INTO {0}(entry_number,username,topic,start_time)
                        VALUES({1},{2},'{3}')
                    '''.format(table, entry_Number, values, t))
            close_commit_connection(connection)

    def send_end_entry(self, table: str, name: str) -> None:
        t = get_time_string()
        cursor, connection = open_connection(self.db)
        cursor.execute('''
            UPDATE {0} SET end_time='{1}' WHERE username='{2}' AND end_time IS NULL
        '''.format(table, t, name))
        close_commit_connection(connection)
        self.send_sesh_length(table, name)

# This will get the session length in a readable format for input into the database or to display to the user
# In the future this will be able to send these signatures to be displayed at end of session
# End time(to numeric) minus Start time(to numeric)
# sesh_length(end_time, start_time) = sesh_length
    def send_sesh_length(self, table: str, name:str) -> None:
        cursor, connection = open_connection(self.db)
        cursor.execute('''
                SELECT start_time, end_time
                FROM {}
                WHERE username='{}' AND session_length IS NULL
            '''.format(table, name))
        query = cursor.fetchone()
        connection.commit()
        start = get_stime_iter(query[0])
        end = get_stime_iter(query[1])
        dic = sesh_length(start, end)
        sesh_input = ''
        for i in dic:
            if dic[i] != 0:
                sesh_input += "{} {}".format(dic[i], i)
                if i != 'Seconds':
                    sesh_input += ','
        #print(query)
        cursor.execute('''
            UPDATE {0} SET session_length='{1}' WHERE username='{2}' AND session_length IS NULL
        '''.format(table, sesh_input, name))
        close_commit_connection(connection)
    
    def getRecentSessionLength(self, username):
        cursor, connection = open_connection(self.db)
        cursor.execute('''
                SELECT session_length
                FROM all_records
                WHERE username="{}"
                ORDER BY entry_number desc
                LIMIT 1
        '''.format(username))
        query = cursor.fetchone()
        close_commit_connection(connection, query)
        return query
