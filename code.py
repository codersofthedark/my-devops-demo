#Benchmarking SQS
from flask import Flask, request
import boto3
import logging
logging.basicConfig(handlers=[logging.StreamHandler()],format='%(asctime)s %(message)s', level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def root():
    logging.debug(request.path)
    logging.debug(request.method)
    logging.info(str(request.headers).replace(chr(10),' '))
    return "Request Completed"



