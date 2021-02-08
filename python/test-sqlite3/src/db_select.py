# -*- coding: utf8 -*-
import cPickle
import sqlite3

# open existing database
conn = sqlite3.connect('my_db.db')

c = conn.cursor()

for num in range(0, 2):
  # print all lines ordered by integer value in my_var2
  for row in c.execute('SELECT * FROM my_db{} ORDER BY my_var2'.format(num)):
    print row,
    if row[4]:
      print cPickle.loads(str(row[4])),
    print

  # print all lines that have "YES" as my_var1 value
  # and have an integer value <= 7 in my_var2
  t = ('YES',7,)
  for row in c.execute('SELECT * FROM my_db{} WHERE my_var1=? AND my_var2 <= ?'.format(num), t):
    print row

  # print all lines that have "YES" as my_var1 value
  # and have an integer value <= 7 in my_var2
  t = ('YES',7,)
  c.execute('SELECT * FROM my_db{} WHERE my_var1=? AND my_var2 <= ?'.format(num), t)
  rows = c.fetchall()
  for r in rows:
    print r

# close connection
conn.close()
