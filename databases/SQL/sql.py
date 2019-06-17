import mysql.connector
import pprint

from dbconfig import dbconfig
import sql_commands

import sql_exec

DB = dbconfig['database']
print('Tables on %s:' % DB)
pprint.pprint(sql_exec.show_tables(dbconfig))

print('Enter table name to create:')
table = input()
if sql_exec.check_table_exists(dbconfig, table):
    print('Entered table %s is already exsists' % table)
else:
    print('Entered table %s doesn\'t exsists' % table)
    tbl_created = sql_exec.create_table(dbconfig, table)
    print('Table has been created' if tbl_created else 'Something go wrong')
    pprint.pprint(sql_exec.describe_table(dbconfig, table))

print('Tables on %s:' % DB)
pprint.pprint(sql_exec.show_tables(dbconfig))


print('%s table content:' % table)
print(sql_exec.select_content(dbconfig, table))


print('Enter table name to delete:')
table = input()
if table is not '':
    tbl_deleted = sql_exec.delete_table(dbconfig, table)
    print('Table deleted')

