# -*- coding: utf8 -*-

import sqlite3

# make connection to existing db
conn = sqlite3.connect('my_db.db')
c = conn.cursor()

for num in range(0, 2):
  # update field
  # SQLite - UPSERT *not* INSERT or REPLACE; http://stackoverflow.com/questions/418898/sqlite-upsert-not-insert-or-replace#comment8249319_4330694
  t = ('NO', 'ID_2352533', )
  c.execute('SELECT id FROM my_db{} WHERE docid=?'.format(num), (t[1],))
  row = c.fetchone()
  c.execute("UPDATE my_db{} SET my_var1=? WHERE id=?".format(num), (t[0], row[0]))
  print "Total number of rows changed:", conn.total_changes
  
  # delete rows
  t = ('NO', )
  c.execute("DELETE FROM my_db{} WHERE my_var1=?".format(num), t)
  print "Total number of rows deleted: ", conn.total_changes
  
  # add column
  c.execute("ALTER TABLE my_db{} ADD COLUMN 'my_var3' TEXT".format(num))
  
  # save changes
  conn.commit()
  
  # print column names
  c.execute("SELECT * FROM my_db{}".format(num))
  col_name_list = [tup[0] for tup in c.description]
  print col_name_list
  
# close connection
conn.close()
