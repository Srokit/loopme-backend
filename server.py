"LoopMe Backend server code"

import random

import boto3
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

s3 = boto3.client('s3')

S3_BACKEND_HOST = 'https://loopme-comb-loops.s3.us-west-1.amazonaws.com/'

def info_from_filename(fn):
    retval = dict()
    parts = fn.split('_')
    parts[-1] = parts[-1].split('.')[0]
    retval['name'] = parts[0]
    retval['tempo'] = parts[1]
    retval['key'] = parts[2]
    return retval

def choose_random_s3_file():
    res = s3.list_objects_v2(Bucket='loopme-comb-loops').get('Contents')
    fn_list = [ obj.get('Key') for obj in res ]
    return random.choice(fn_list)

@app.route('/loop')
def get_loop():
    fn = choose_random_s3_file()
    loop_info = info_from_filename(fn)
    return {'url': S3_BACKEND_HOST + fn,
            'info': loop_info}
