# -*- coding: utf8 -*-
import cPickle
import sqlite3

# https://docs.python.org/2/library/sqlite3.html
# http://www.tutorialspoint.com/sqlite/
# SQLite - Working with large data sets in Python effectively; http://sebastianraschka.com/Articles/sqlite3_database.html

conn = sqlite3.connect('my_db.db')
c = conn.cursor()

# http://stackoverflow.com/questions/198692/can-i-pickle-a-python-dictionary-into-a-sqlite3-text-field
multi_lines = [('ID_2352533','YES', 1, sqlite3.Binary(cPickle.dumps({u'a': 1}, cPickle.HIGHEST_PROTOCOL))),
               ('ID_2352534','NO', 0, sqlite3.Binary(cPickle.dumps({u'b': 2}, cPickle.HIGHEST_PROTOCOL))),
               ('ID_2352535','YES', 3, sqlite3.Binary(cPickle.dumps({u'c': 3}, cPickle.HIGHEST_PROTOCOL))),
               ('ID_2352536','YES', 9, sqlite3.Binary(cPickle.dumps({u'a': 0, u'd': 4}, cPickle.HIGHEST_PROTOCOL))),
               ('ID_2352537','YES', 10, sqlite3.Binary(cPickle.dumps({u'a': 1}, cPickle.HIGHEST_PROTOCOL)))
               ]
for num in range(0, 2):
  c.execute('DELETE FROM my_db{}'.format(num))
  c.execute('DROP TABLE my_db{}'.format(num))
  # SQLite3에서의 AUTO_INCREMENT; http://blog.arzz.com/411
  # Datatypes In SQLite Version 3; https://www.sqlite.org/datatype3.html
  c.execute('CREATE TABLE my_db{} (id PRIMARY KEY, docid TEXT, my_var1 TEXT, my_var2 INT, my_dict BLOB)'.format(num))

  c.execute("INSERT INTO my_db{} (docid, my_var1, my_var2) VALUES ('ID_2352532', 'YES', 4)".format(num))
  c.executemany('INSERT INTO my_db{} (docid, my_var1, my_var2, my_dict) VALUES (?,?,?,?)'.format(num), multi_lines)

conn.commit()
conn.close()
