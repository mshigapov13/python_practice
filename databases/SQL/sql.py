import mysql.connector
import pprint

from dbconfig import dbconfig
import sql_commands

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
DB = dbconfig['database']
table = input()

_SQL = sql_commands.show_table + DB
cursor.execute(_SQL)
res = cursor.fetchall()
tables = [x for y in res for x in y]

print('Tables on %s:' % DB)
pprint.pprint(tables)


table_exists = True if table in tables else False
table_exists_text = ('is already' if table_exists else 'doesn\'t') + ' exists'

print('Entered table %s ' % table + table_exists_text)
if not table_exists:
    _SQL = sql_commands.create_table % table
    cursor.execute(_SQL)
    print('Table %s has been created' % table)

_SQL = sql_commands.describe_table % (DB, table)
cursor.execute(_SQL)
print('Description of %s table' % table)
pprint.pprint(cursor.fetchall())

_SQL = sql_commands.select % (DB,table)
res = cursor.execute(_SQL)
print('Content %s table:' % table)
pprint.pprint(res)