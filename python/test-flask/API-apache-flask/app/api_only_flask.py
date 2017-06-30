# -*- coding: utf8 -*-
from app import app
from flask import Flask
from flask import request
import os
import logging
import mod_wsgi


# user configuration
# http://michal.karzynski.pl/blog/2013/09/14/django-in-virtualenv-on-webfactions-apache-with-mod-wsgi/
MY_VAL1 = os.environ.get('MY_KEY1')
MY_VAL2 = os.environ.get('MY_KEY2')

@app.route('/')
def api_root():
  # https://stackoverflow.com/questions/20789391/django-referencing-different-settings-files-from-wsgi-depending-on-server
  # http://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
  # mod_wsgi.process_group value comes from WSGIProcessGroup on apache-flask3.conf
  return 'Welcome {}\t{}\t{}'.format(mod_wsgi.process_group, MY_VAL1, MY_VAL2)


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
  return 'insert id {} {}'.format(id, sentence.encode('utf8'))


@app.route('/select/<id>')
def select(id):
  return 'select id {}'.format(id)


@app.route('/update/<id>')
def update(id):
  return 'update id {}'.format(id)


@app.route('/delete/<id>')
def delete(id):
  return 'delete id {}'.format(id)


@app.route('/stop')
def stop():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
    raise RuntimeError('Not running with the Werkzeug Server')
  func()
  return 'stop'
