"LoopMe Backend server code"

import random

from flask import Flask, send_from_directory
from flask_cors import CORS

from data import loop_filename_from_info, get_comb_loop_infos_from_folder

app = Flask(__name__)

CORS(app)

@app.route('/loop')
def get_loop():
    loop_infos = get_comb_loop_infos_from_folder()
    loop_info = random.choice(loop_infos)
    return {'url': '/combined_loops/{}'.format(loop_filename_from_info(loop_info)),
            'info': loop_info}

@app.route('/combined_loops/<path:path>')
def get_a_loop(path):
    return send_from_directory('combined_loops', path)
