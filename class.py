import sqlite3
import os
import psycopg3


class Pass:
    def __init__(self, name, height, coordinates, description):
            self.name = name
            self.height = height
            self.coordinates = coordinates
            self.description = description

    def save_to_database(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS passes
                                  (name TEXT, mountain TEXT, altitude REAL,
                                   latitude REAL, longitude REAL, description TEXT)''')
        cursor.execute('INSERT INTO passes VALUES (?, ?, ?, ?, ?, ?)',
                       (self.name, self.height, self.coordinates, self.description))
        conn.commit()
        conn.close()
        pass


class Database:
    def __init__(self):
        self.host = os.environ.get('FSTR_DB_HOST')
        self.port = os.environ.get('FSTR_DB_PORT')
        self.login = os.environ.get('FSTR_DB_LOGIN')
        self.password = os.environ.get('FSTR_DB_PASS')
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg3.connect(
                host=self.host,
                port=self.port,
                user=self.login,
                password=self.password
            )
        except psycopg3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def add_new_record(self, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Passes (status) VALUES ('new')")
            self.connection.commit()
            cursor.close()
        except psycopg3.Error as e:
            print(f"Error adding new record: {e}")