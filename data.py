# import pandas as pd 
# import sqlite3
# import chardet
# from DbConn import coxn
# # book = xlrd.open_workbook("Prince Pipe Flat File_2710.csv")
# # sheet = book.sheet_by_name()
# # print(sheet)

# # conn = sqlite3.connect('test_database')
# # c = conn.cursor()
# # c.execute('CREATE TABLE IF NOT EXISTS products (product_name text, price number)')



# # data = pd.read_csv('/Users/apple/Desktop/pandas//Prince Pipe Flat File_2710.csv', encoding='ISO-8859-1')
# # a = data.head()
# # print(a)

# df = pd.read_excel('sportsref_download.xlsx', engine = 'openpyxl')
# try:
#    df.to_sql('EPL_LOG',con=coxn,if_exists='replace')

# except:
#     pass
#     print("Failed!")

# else:
#     print("saved in the table")
# print(df)

# import sqlalchemy as sa

# from SQLAlchemy import create_engine
# db_uri = "SQLite:/apple/Desktop/pandas/Price.db"
# eng = create_engine(db_uri)
# from pandas.core.frame import DataFrame
# import pandas as pd
# from DbConn import coxn

# 1.-Load module
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

# import pandas as pd
#2.-Turn on database engine
db_uri = "sqlite:////Users/apple/Desktop/pandas/db1.db"
eng = create_engine(db_uri)

# # eng.execute('CREATE TABLE "prince_data"')
# with eng.engine.begin() as conn:
#     result = conn.execute(text('CREATE TABLE prince_data'))

query = 'CREATE TABLE prince_data'
with eng.pool.connect() as db_conn:
     db_conn.execute(text(query))
# df = pd.read_excel('Users/apple/Desktop/pandas/1.csv', engine = 'openpyxl')
 
# try:
#    df.to_sql('EPL_LOG',con=coxn,if_exists='replace')

# except:
#     pass
#     print("Failed!")

# else:
#     print("saved in the table")
# print(df)