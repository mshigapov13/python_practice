import mysql.connector
import pprint

from dbconfig import dbconfig
import sql_commands
from show_tables import show_tables

def check_table_exists(table: str) ->
tables = show_tables(dbconfig)





conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
DB = dbconfig['database']




_SQL = sql_commands.show_table + DB
cursor.execute(_SQL)
res = cursor.fetchall()
tables = [x for y in res for x in y]

print('Tables on %s:' % DB)
pprint.pprint(tables)

table_exists = True if table in tables else False
table_exists_text = ('is already' if table_exists else 'doesn\'t') + ' exists'

print('Entered table %s ' % table + table_exists_text)
