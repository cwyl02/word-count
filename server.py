from flask import Flask, request
import os

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
import time

import lib
import monitor

METRICS_PATH = os.getenv('PROMETHEUS_PATH', '/metrics')

app = Flask(__name__)
# run Prometheus metric server
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
   METRICS_PATH : make_wsgi_app()
})
app.before_request(monitor.before_request)
app.after_request(monitor.after_request)

FILE_FORM_FIELD = os.environ.get('FILE_FORM_FIELD', 'data')

@app.route('/')
def index():
    return "please use POST to feed me the file"

@app.route('/', methods=['POST'])
def count_words_from_upload():
    uploaded_file = request.files[FILE_FORM_FIELD]
    response = {'wordCount': -1}
    if uploaded_file.filename != '':
        response['wordCount'] = lib.calculate(uploaded_file)
        response['fileName'] = uploaded_file.filename
    
    monitor.FILES_COUNTED.labels(response['fileName'], response['wordCount']).inc()
    return response
