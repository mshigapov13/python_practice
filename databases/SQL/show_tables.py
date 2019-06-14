from DBcm import UseDatabase
from typing import List


from dbconfig import dbconfig
import sql_commands


def show_tables(config: dict) -> List:
    with UseDatabase(config) as cursor:
        _SQL = sql_commands.show_table + config['database']
        cursor.execute(_SQL)
        res = cursor.fetchall()
        return [table for sub_item in res for table in sub_item]


def check_table_exists(table: str) -> bool:
    tables = show_tables(dbconfig)
    return table in tables
