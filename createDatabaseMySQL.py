 # -*- coding: utf-8 -*-
"""

Creating a MySQL Database in Python // macOS
@author: AdamGetbags

"""

# https://dev.mysql.com/downloads/mysql/
# https://dev.mysql.com/downloads/workbench/

# pip install SQLAlchemy

#import modules
import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
# import mysqlclient

#confirm install
# check SQL Alchemy version
print(sqlalchemy.__version__)
print(os.getcwd())

# create data 
symbols = ['GOOG', 'GOOG', 'AAPL', 'AAPL', 'AMZN', 'AMZN']
dates = [
    '12-13-2022', '12-14-2022', 
    '12-13-2022', '12-14-2022', 
    '12-13-2022', '12-14-2022'
]
prices = [100, 101, 102, 103, 104, 105]

# create dataframe
data = pd.DataFrame(list(zip(symbols, dates, prices)),
    columns =['symbol', 'date', 'price'])

# db credentials 
usr = 'userName'
pwd = 'password'
host = '127.0.0.1'
port = 6969
dbName = 'dbName'
tableName = 'tableName'

# create engine object
engine = create_engine(
    f"mysql+mysqldb://{usr}:{pwd}@{host}:{port}/{dbName}", 
    echo=True, 
    future=True)

# create table
data.to_sql(name=tableName, con=engine, if_exists='replace')

'''
engine.connect() has auto ROLLBACK
engine.begin() has auto COMMIT
''' 

# get a connection / get column names // auto ROLLBACK
with engine.connect() as conn:
    result = conn.execute(text("DESCRIBE dataTable;"))
    for row in result:
        print(row)

# get a connection / fetch rows // auto ROLLBACK
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM dataTable"))
    for row in result:
        print(f"""
              index: {row.index}
              symbol: {row.symbol} 
              date: {row.date} 
              price: {row.price}
              """)
              
# # get a connection / drop a table // autocommit
# with engine.begin() as conn:
#     conn.execute(
#         text("DROP TABLE dataTable"))
                 
# # close all checked in database connections 
# engine.dispose() 
