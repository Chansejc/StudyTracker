from ST_time import *
import time as time
import sqlite3 as sql
from Utils import *


def open_connection(db):
    connection = sql.connect(f'{db}.db')
    cursor = connection.cursor()
    return cursor, connection


def close_commit_connection(connection, query=()):
    connection.commit()
    connection.close()
    print(query)


def get_time_string():
    import time
    t = time.ctime()
    t = t[11:19]
    return t


class Database:
    def __init__(self, db: object, tables: object) -> None:
        self.self = self
        self.db = db
        self.tables = tables

    def get_entries(self, table: object) -> object:

        if table in self.tables:
            cursor, connection = open_connection(self.db)
            cursor.execute('''
                SELECT * FROM {}
                '''.format(table))
            query = cursor.fetchall()
            close_commit_connection(connection, query)
            return query

        else:
            print("Query Unsuccessful. Table not in Database.")
            return

    def send_entry(self, table: str, values: list) -> None:
        to_add = list_to_entry(values)
        if table in self.tables:
            cursor, connection = open_connection(self.db)
            cursor.execute('''
                INSERT INTO {0}
                VALUES({1})
            '''.format(table, to_add))
            close_commit_connection(connection)
        else:
            print("Query Unsuccessful. Table not in database")

    def send_start_entry(self, table: str, values: list):
        t = get_time_string()
        values = list_to_entry(values)
        print(values)
        if table in self.tables:
            cursor, connection = open_connection(self.db)
            cursor.execute('''
                        INSERT INTO {0}(username,topic,start_time)
                        VALUES({1},'{2}')
                    '''.format(table, values, t))
            close_commit_connection(connection)
        else:
            print("Query Unsuccessful. Table not in database")

    def send_end_entry(self, table: str, name: str) -> None:
        t = get_time_string()
        cursor, connection = open_connection(self.db)
        cursor.execute('''
            UPDATE {0} SET end_time='{1}' WHERE username='{2}' AND end_time IS NULL
        '''.format(table, t, name))
        close_commit_connection(connection)
        self.send_sesh_length(table, name)

    def send_sesh_length(self, table, name):
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
        print(query)
        print(sesh_input)
        cursor.execute('''
            UPDATE {0} SET session_length='{1}' WHERE username='{2}' AND session_length IS NULL
        '''.format(table, sesh_input, name))
        close_commit_connection(connection)

    def current_user(self, name):
        db = self.db
        trie = Trie()
        lst_of_records = db.get_entries('records')
        names = [i[0] for i in lst_of_records]
        for i in names:
            trie.insert(i)
        return trie.search(name)


'''
Building Trie Entities
- Used for searching and creating users
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for i, c in enumerate(word):
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c in cur.children:
                print(cur.children)
                cur = cur.children[c]
            else:
                return "Item not in list"

        return "Item in list"

    def starts_with(self, word):
        cur = self.root

        for c in word:
            if c in cur.children and not cur.children[c].endOfWord:
                print(cur.children)
                cur = cur.children[c]
            else:
                return "Item not in list"

        return "Item in list"
