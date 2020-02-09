import sqlite3
from datetime import datetime


class Database():

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS temps (id INTEGER PRIMARY KEY, datetime INTEGER, temperature REAL, humidity REAL, temp_inside REAL, hum_inside REAL)")
        self.connection.commit()


    def insert(self, temperature=None, humidity=None, temp_inside=None, hum_inside=None):

        self.creation_date = datetime.now(tz=None)
        self.datetime_stamp = self.creation_date.strftime('%s') #integer datetime object
        #self.connection
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO temps VALUES (NULL, ?,?,?,?,?)", (self.datetime_stamp, temperature, humidity, temp_inside, hum_inside))
        self.connection.commit()
        #print("connection commiting")
        #self.cursor.lastrowid = last_id
        #self.connection.close()
        #print("connection closed")

    def view_table(self):

        self.cursor.execute("SELECT * FROM temps")
        self.rows = self.cursor.fetchall()
        #connection.close()
        return self.rows

    def commit(self):
        self.connection.commit()
    def close(self):
        self.connection.close()
