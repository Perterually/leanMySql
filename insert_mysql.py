#!/usr/bin/env python
# encoding: utf-8

import MySQLdb

conn = MySQLdb.connect('localhost','root','root','demo')
cur = conn.cursor()
value = []
for li in range(21):
    value.append((li,'hi'))
cur.executemany('insert into text values(%s,%s)',value)
conn.commit()

