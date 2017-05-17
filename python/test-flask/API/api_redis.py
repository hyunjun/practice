# -*- coding: utf8 -*-
from flask import Flask
from flask import request
import logging
import redis
import socket


conn = redis.StrictRedis(host='redis server', port=16379, db=0)
HASH_NAME = 'sentence'
app = Flask(__name__)


@app.route('/')
def api_root():
  return 'Welcome'


@app.route('/count')
def count():
  cnt = 0
  cnt = conn.hlen(HASH_NAME)
  app.logger.debug(cnt)
  return 'count {}'.format(cnt)


# curl -XPOST http://x.y.z.w:59460/insert/123 -d "{\"test\": \"값\"}"
'''
@app.route('/insert/<id>', methods=['POST'])
def insert(id):
  j = request.get_json(force=True)
  app.logger.debug(j)
  return 'insert id {}'.format(id)
'''
# curl -XPUT http://x.y.z.w:59460/insert/123 -F sentence="테스트 문장"
@app.route('/insert/<id>', methods=['PUT'])
def insert(id):
  sentence = request.form['sentence']
  app.logger.debug(sentence)
  conn.hset(HASH_NAME, id, sentence)
  return 'insert id {} {}'.format(id, sentence.encode('utf8'))


@app.route('/select/<id>')
def select(id):
  sentence = conn.hget(HASH_NAME, id)
  return 'select id {} sentence {}'.format(id, sentence)


@app.route('/update/<id>', methods=['PUT'])
def update(id):
  sentence = request.form['sentence']
  app.logger.debug(sentence)
  conn.hset(HASH_NAME, id, sentence)
  return 'update id {} sentence {}'.format(id, sentence.encode('utf8'))


@app.route('/delete/<id>')
def delete(id):
  conn.hdel(HASH_NAME, id)
  return 'delete id {}'.format(id)


@app.route('/stop')
def stop():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  global conn
  del conn
  func()
  return 'stop'


if __name__ == '__main__':
  IP_ADDRESS = socket.gethostbyname(socket.gethostname())
  app.logger.setLevel(logging.DEBUG)
  app.run(host=IP_ADDRESS, port=59460, debug=True)
