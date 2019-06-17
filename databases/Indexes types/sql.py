import mysql.connector
import time
from DBcm import UseDatabase
from dbconfig import dbconfig
import sql_commands
from datetime import date
from random import randint

table_names = ['common_people', 'btree_people', 'hash_people']

with UseDatabase(dbconfig) as cursor:
    _SQL = sql_commands.Common_table_create % (dbconfig['database'], table_names[0])
    cursor.execute(_SQL)
    _SQL = sql_commands.BTree_table_create % (dbconfig['database'], table_names[1])
    cursor.execute(_SQL)
    _SQL = sql_commands.Hash_table_create % (dbconfig['database'], table_names[2])
    cursor.execute(_SQL)

    start_dt = date.today().replace(year=2002).toordinal()
    end_dt = date.today().replace(year=2018).toordinal()
    gender = ['m', 'f']
    for i in range(0, 10001):
        if i % 10 == 0:
            l_name = (chr(randint(ord('a'), ord('z'))) * 10) * 2
            f_name = l_name
        else:
            l_name = chr(randint(ord('a'), ord('z'))) * 10
            f_name = chr(randint(ord('a'), ord('z'))) * 10
        dob = str(date.fromordinal(randint(start_dt, end_dt)))
        rand_gender = gender[randint(0, 1)]
        for table in table_names:
            _SQL = sql_commands.table_insert % (dbconfig['database'], table, i, l_name, f_name, dob, rand_gender)
            cursor.execute(_SQL)

    for table in table_names:
        start_time = time.time()
        _SQL = sql_commands.select % (dbconfig['database'], table)
        cursor.execute(_SQL)
        cursor.fetchall()
        print('%s executed: --- %s ---' % (table, time.time() - start_time))

    for table in table_names:
        _SQL = sql_commands.table_drop % (dbconfig['database'], table)
        cursor.execute(_SQL)




'''
import common_table
import btree
import hash_table



start_time = time.time()
common_table.select()
print('Non-index executed: --- %s ---' % (time.time() - start_time))


start_time = time.time()
btree.select()
print('btree-index executed: --- %s ---' % (time.time() - start_time))


start_time = time.time()
hash_table.select()
print('hash-index executed: --- %s ---' % (time.time() - start_time))


with UseDatabase(dbconfig) as cursor:
    for table in table_names:
        _SQL = sql_commands.table_drop % (dbconfig['database'], table)
        cursor.execute(_SQL)
'''