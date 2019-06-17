from DBcm import UseDatabase
from typing import List

import sql_commands


def show_tables(config: dict) -> List:
    with UseDatabase(config) as cursor:
        _SQL = sql_commands.show_table + config['database']
        cursor.execute(_SQL)
        res = cursor.fetchall()
        return [table for sub_item in res for table in sub_item]


def check_table_exists(config: dict, table: str) -> bool:
    tables = show_tables(config)
    return table in tables


def create_table(config: dict, table: str) -> bool:
    with UseDatabase(config) as cursor:
        _SQL = sql_commands.create_table % table
        cursor.execute(_SQL)
    return check_table_exists(config, table)


def delete_table(config: dict, table: str) -> bool:
    with UseDatabase(config) as cursor:
        _SQL = sql_commands.delete % table
        cursor.execute(_SQL)
    return check_table_exists(config, table)


def select_content(config: dict, table: str) -> List:
    with UseDatabase(config) as cursor:
        _SQL = sql_commands.select % (config['database'], table)
        cursor.execute(_SQL)
        return cursor.fetchall()


def describe_table(config: dict, table: str) -> List:
    with UseDatabase(config) as cursor:
        _SQL = sql_commands.describe_table % (config['database'], table)
        cursor.execute(_SQL)
        return cursor.fetchall()


