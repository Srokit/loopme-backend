"LoopMe Backend server code"

from flask import Flask, send_from_directory, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

NUM_LOOPS = 5

loop_infos = [
    {
        'name': 'Linda',
        'tempo': '135',
        'key': 'C#m'
    },
    {
        'name': 'Rita',
        'tempo': '140',
        'key': 'Dmaj'
    },
    {
        'name': 'Faith',
        'tempo': '120',
        'key': 'Em'
    },
    {
        'name': 'Rachel',
        'tempo': '155',
        'key': 'C#m'
    },
    {
        'name': 'Annita',
        'tempo': '130',
        'key': 'A#maj'
    },
]

@app.route('/loop')
def get_loop():
    last_loop_index = request.args.get('last_loop', None)
    print(request.args)
    if last_loop_index is None:
        raise Exception
    last_loop_index = int(last_loop_index)
    curr_index = (last_loop_index + 1) % NUM_LOOPS
    return {'index': str(curr_index),
            'url': '/loops/loop_{}.mp3'.format(curr_index),
            'info': loop_infos[curr_index]}

@app.route('/loops/<path:path>')
def get_a_loop(path):
    return send_from_directory('loops', path)
