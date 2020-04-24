import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''create table cadatro(id int(5), nome varchar(50) not null, email varchar(50), primary key (id))''')
c.execute('select * from sqlite_master as m, pragma_table_info(m.name)')

for row in c.fetchall():
    print('coluna: ', row[6])
    print('notnull: ', row[8])
    print('pk: ', row[10])
