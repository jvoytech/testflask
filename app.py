#!/usr/bin/env python

import os, json
import configparser
from flask import Flask, render_template

from mgr import ManagedMySqlContext, ManageMySqlCursor

mysql_cfg = {}

config = configparser.ConfigParser()
config.read('db.ini')
mysql_cfg.update(**config['DEFAULT'])

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    
    with ManagedMySqlContext(mysql_cfg) as ctx:
        with ManageMySqlCursor(ctx) as cursor:
            
            query = 'select * from Author where AuthorID < 1008'
            cursor.execute(query)
            text = list(cursor)
    
    name = 'booksdb.Author'
    return render_template('hello.html', data = text, name=name)

@app.after_request
def set_res_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
