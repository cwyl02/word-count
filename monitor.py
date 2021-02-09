from prometheus_client import Counter, Summary

REQUEST_COUNT = Counter('request_count', "Number of total word count request received")
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing word count request')

