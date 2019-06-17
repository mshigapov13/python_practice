Common_table_create = '''
create table if not exists %s.%s(
id int,
last_name varchar(50),
first_name varchar(50),
dob date,
gender enum('m','f')
)
'''

BTree_table_create = '''
create table if not exists %s.%s(
id int,
last_name varchar(50),
first_name varchar(50),
dob date,
gender enum('m','f'),
key (last_name, first_name, dob)
)'''

Hash_table_create = '''
create table if not exists %s.%s(
id int,
last_name varchar(50),
first_name varchar(50),
dob date,
gender enum('m','f'),
key using hash(last_name)
)'''


table_insert = '''insert into %s.%s values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')'''

table_drop = '''drop table %s.%s'''

select = 'select count(last_name) from %s.%s where last_name = first_name'
