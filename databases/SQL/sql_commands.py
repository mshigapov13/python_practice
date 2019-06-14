
show_table = 'show tables from '

create_table = '''create table if not exists %s (
task_id int auto_increment primary key,
title varchar(255) not null,
solved varchar(255) not null)'''

describe_table = 'describe %s.%s'

select = 'select * from %s.%s'