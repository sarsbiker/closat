'''
创建数据表
'''
import sqlite3

conn = sqlite3.connect('closat.db')

c = conn.cursor()

c.execute('''create table if not exists cards 
        (id int primary key not null,
        cardname text not null unique,
        type text not null,
        detail text);''')

conn.commit()
conn.close()

