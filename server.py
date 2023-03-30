"LoopMe Backend server code"

from flask import Flask, send_from_directory
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

# increments to 4 and then back down to 0 to represent 5 loops
# Starts on last index so that the first call will play loop 0
loop_index = 4

def increment_loop_index():
    global loop_index
    loop_index = (loop_index + 1) % NUM_LOOPS

@app.route('/loop')
def get_loop():
    increment_loop_index()
    return {'url': '/loops/loop_{}.mp3'.format(loop_index),
            'info': loop_infos[loop_index]}

@app.route('/loops/<path:path>')
def get_a_loop(path):
    return send_from_directory('loops', path)
