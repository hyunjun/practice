# -*- coding: utf8 -*-
from flask import Flask
from flask import request
import logging
import MySQLdb
import socket


conn = MySQLdb.connect(host='mysql server', user='test_user', passwd='testpwd', db='test_db', port=3306)
conn.set_character_set('utf8')
conn.autocommit(True)
cursor = conn.cursor(cursorclass=getattr(MySQLdb.cursors, 'Cursor'))
app = Flask(__name__)


@app.route('/')
def api_root():
  return 'Welcome'


@app.route('/count')
def count():
  cnt = 0
  # cursor.execute('desc sentence')
  # app.logger.debug(cursor._executed)
  cursor.execute('select count(*) from sentence')
  app.logger.debug(cursor._executed)
  recs = cursor.fetchall()
  app.logger.debug(recs)
  cnt = recs[0][0]
  return 'count {}'.format(cnt)


# curl -XPOST http://x.y.z.w:59459/insert/123 -d "{\"test\": \"값\"}"
'''
@app.route('/insert/<id>', methods=['POST'])
def insert(id):
  j = request.get_json(force=True)
  app.logger.debug(j)
  return 'insert id {}'.format(id)
'''
# curl -XPUT http://x.y.z.w:59459/insert/123 -F sentence="테스트 문장"
@app.route('/insert/<id>', methods=['PUT'])
def insert(id):
  sentence = request.form['sentence']
  app.logger.debug(sentence)
  cursor.execute('INSERT INTO sentence (id, sentence) VALUES (%s, %s)', (id, sentence))
  return 'insert id {} {}'.format(id, sentence.encode('utf8'))


@app.route('/select/<id>')
def select(id):
  cursor.execute('SELECT sentence FROM sentence where id = %s', (id,))
  recs = cursor.fetchall()
  app.logger.debug(recs)
  if 0 != len(recs):
    return 'select id {} {}'.format(id, recs[0][0])
  return 'select id {} NOT EXIST'.format(id)


@app.route('/update/<id>', methods=['PUT'])
def update(id):
  sentence = request.form['sentence']
  app.logger.debug(sentence)
  cursor.execute('UPDATE sentence SET sentence = %s where id = %s', (sentence, id))
  return 'update id {} sentence {}'.format(id, sentence.encode('utf8'))


@app.route('/delete/<id>')
def delete(id):
  cursor.execute('DELETE FROM sentence where id = %s', (id,))
  return 'delete id {}'.format(id)


@app.route('/stop')
def stop():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  cursor.close()
  conn.close()
  func()
  return 'stop'


if __name__ == '__main__':
  IP_ADDRESS = socket.gethostbyname(socket.gethostname())
  app.logger.setLevel(logging.DEBUG)
  app.config.from_pyfile('settings.cfg')
  DEBUG = app.config['DEBUG']
  app.run(host=IP_ADDRESS, port=59459, debug=DEBUG)
