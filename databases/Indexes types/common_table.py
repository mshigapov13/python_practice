import mysql.connector
from DBcm import UseDatabase
from dbconfig import dbconfig
import sql_commands
from datetime import date
from random import randint


def common_table() -> None:
    with UseDatabase(dbconfig) as cursor:
        table_name = 'common_people'
        _SQL = sql_commands.Common_table_create % (dbconfig['database'], table_name)
        cursor.execute(_SQL)
        start_dt = date.today().replace(year=2002).toordinal()
        end_dt = date.today().replace(year=2018).toordinal()
        gender = ['m', 'f']
        for i in range(0, 10001):
            if i%10 == 0:
                l_name = (chr(randint(ord('a'), ord('z')))*10) * 2
                f_name = l_name
            else:
                l_name = chr(randint(ord('a'), ord('z')))*10
                f_name = chr(randint(ord('a'), ord('z')))*10
            dob = str(date.fromordinal(randint(start_dt, end_dt)))
            rand_gender = gender[randint(0, 1)]
            _SQL = sql_commands.table_insert % (dbconfig['database'],table_name, i, l_name, f_name, dob, rand_gender)
            cursor.execute(_SQL)

def delete() -> None:
    with UseDatabase(dbconfig) as cursor:
        table_name = 'common_people'
        _SQL = sql_commands.table_drop % (dbconfig['database'],table_name)
        cursor.execute(_SQL)


def select() -> None:
    with UseDatabase(dbconfig) as cursor:
        table_name = 'common_people'
        _SQL = sql_commands.select % (dbconfig['database'], table_name)
        cursor.execute(_SQL)
        cursor.fetchall()