# -*- coding: utf8 -*-
from flask import Flask
from flask import request
from flask_pytest import FlaskPytest
import logging
import os
import sys


sys.path.append(os.path.join(os.path.dirname('.'), '..'))


from common.src import common


logger = logging.getLogger('api')
common.setup_logging(os.environ.get('LOGGING_CONFIG_FILEPATH'))


app = Flask(__name__)
app.config.from_pyfile('settings.py')
app = FlaskPytest(app)


@app.route('/')
def api_root():
  return 'Welcome'


@app.route('/add/<int:left>/<int:right>')
def add(left, right):
  return str(left + right)


@app.route('/count')
def count():
  return 'count'


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
  logger.info('insert id {} {}'.format(id, sentence.encode('utf8')))
  return 'insert id {} {}'.format(id, sentence.encode('utf8'))


@app.route('/select/<id>')
def select(id):
  logger.debug('select id {}'.format(id))
  return 'select id {}'.format(id)


@app.route('/update/<id>')
def update(id):
  logger.info('update id {}'.format(id))
  return 'update id {}'.format(id)


@app.route('/delete/<id>')
def delete(id):
  logger.debug('delete id {}'.format(id))
  return 'delete id {}'.format(id)


@app.route('/stop')
def stop():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()
  return 'stop'


if __name__ == '__main__':
  # IP_ADDRESS = socket.gethostbyname(socket.gethostname())
  app.logger.setLevel(logging.DEBUG)
  # app.run(host=IP_ADDRESS, port=59459, debug=True)
  app.run(host='0.0.0.0', debug=True)
