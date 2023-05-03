import sqlite3 as DB

CONNECTION = DB.connect('user_data.db')

CURSOR = CONNECTION.cursor()

CURSOR.execute('''
CREATE TABLE IF NOT EXISTS users (
USERNAME TEXT PRIMARY KEY, 
USER_KEY TEXT,
LEVEL TEXT,
EXP TEXT,
MAX_HEALTH TEXT,
DEFENSE TEXT,
LIFE_REGEN TEXT,
ATTACK TEXT
)''')

DATABASE_LIST = ['USERNAME', 'USER_KEY', 'LEVEL', 'EXP', 'MAX_HEALTH', 'DEFENSE', 'LIFE_REGEN', 'ATTACK']

class database:
    def __init__(self, database_name, table):
        self.database_name = database_name
        self.table = table
        pass

    def Insert(self, data, value):
        self.INFO = DATABASE_LIST[data]
        self.VALUE = value
        CURSOR.execute('''INSERT INTO user (INFO) VALUES (VALUE)''')
        pass


CONNECTION.commit()
CONNECTION.close()