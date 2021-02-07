from flask import Flask, request
import os

import lib


app = Flask(__name__)

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

# if __name__ == "__main__":
#     app.run(port=5000)