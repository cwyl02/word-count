from prometheus_client import Counter, Summary
from flask import request
import time

HTTP_REQUEST_COUNT = Counter('request_count',
                        "Number of total HTTP requests received",
                        ['method', 'endpoint', 'http_status'])
FILES_COUNTED = Counter('files_counted',
                        "Number of total word count request received",
                        ['filename', 'wordCount'])
REQUEST_TIME = Summary('request_processing_seconds', 
                        'Time spent processing word count request',
                        ['method', 'endpoint'])

def before_request():
    request.start_time = time.time()

def after_request(response):
    request_time = time.time() - request.start_time
    REQUEST_TIME.labels(request.method, request.path).observe(request_time)
    HTTP_REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    return response
