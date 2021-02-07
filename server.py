from flask import Flask, request
import os
import sys
import signal

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
import time

import lib


app = Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

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
        
    return response

### Non Flask
# def handler():
#     print("word-count service received SIGTERM! exiting...")
#     sys.exit(1)

# if __name__ == "__main__":
#     # gracefully handle interrupt/termination
#     signal.signal(signal.SIGINT, handler)
#     signal.signal(signal.SIGTERM, handler)

#     # start monitoring server
    

#     # start word count flask server
#     app.run(port=5000)