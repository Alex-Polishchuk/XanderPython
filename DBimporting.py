# Importing a csv file to sql DB and Pandas dataframe
import pandas as pd
import sqlite3 as sql
from sqlalchemy import create_engine

#path = str(input("Input the path of the file you want "))
Apath =r"C:\Users\AlexanderTkachenko\OneDrive - JCW Resourcing\Desktop\Xander\Code\Python\Hackathon\hackathon\Databases\Cycling.csv"
Hpath = r""
class database:

    def __init__(self, path):
        #Initialise class. Create path and data variable        
        self.path = path
        readCSV = pd.read_csv(self.path)
        data = pd.DataFrame(readCSV)   
        self.data = data 

        #Shows the number of columns, and rows in the table
    def table_columns(self):
        print("Number columns are", len(self.data.columns.values), ". The column names are", self.data.columns.values)
        print("The number of rows in the table is provided", len(self.data.index))
        print(self.data)

    def create_db(self):
        #Creating a database and connects to sql, if DB already made ignore
        #ERROR
        engine = create_engine('sqlite:///testData.db', echo=True)
        with engine.connect() as conn, conn.begin():
            table_name = 'testTable'
            if engine.dialect.has_table(conn, table_name):
                conn.execute(f'DROP TABLE {table_name}')
            self.data.to_sql(table_name, con=conn)

    def column_type_check(self):
        print(self.data.dtypes)


    def pdToSql (self):
        pass

    def check_missing_values(self):
        for col in self.data.columns:
            miss = self.data[col].isnull().sum()
            if miss>0:
                print("{} has {} missing value(s)".format(col,miss))
            else:
                print("{} has NO missing value!".format(col))

source_DB = database(Apath)
source_DB.table_columns()
source_DB.column_type_check()
source_DB.create_db()

#Opens sql connection, makes the cursor too
source_conn = sql.connect("testData.db")
source_cursor = source_conn.cursor()
#Opens sql destinaltion
dest_conn = sql.connect('testDestination.db')
dest_cursor = dest_conn.cursor()

#Names the tables in the source
table_names = []
for row in source_cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\';'):
    table_names.append(row[0])

#Iterates through and gets the names for each table
for table_name in table_names:
    columns = []
    column_types = []
    for row in source_cursor.execute('PRAGMA table_info({})'.format(table_name)):
        columns.append(row[1])
        column_types.append(row[2])

    #creates a new table if a table doesn't exist already
    create_table_sql = 'CREATE TABLE IF NOT EXISTS {}('.format(table_name)

    for i, column in enumerate(columns):
        create_table_sql += '{} {},'.format(column, column_types[i])
    create_table_sql = create_table_sql[:-1] + ')'

    dest_cursor.execute(create_table_sql)

    source_cursor.execute('SELECT * FROM {}'.format(table_name))
    data = source_cursor.fetchall()

    for row in data:
        new_row = []

        for i, value in enumerate(row):
            try:
                if column_types[i] == 'INTEGER':
                    new_row.append(int(value))
                else:
                    column_types[i] == 'REAL'
                    new_row. append(float(value))
            except ValueError:
                new_row.append(value)

        dest_cursor.execute('INSERT INTO {} VALUES ({})'.format(table_name, ','.join(['?' for i in range(len(columns))])), tuple(new_row))

dest_conn.commit()
source_cursor.close()
source_conn.close()
dest_cursor.close()
dest_conn.close()
