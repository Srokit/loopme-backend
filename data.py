import os

def loop_filename_from_info(loop_info):
    return '{}_{}_{}.mp3'.format(loop_info['name'], loop_info['tempo'], loop_info['key']).replace(' ', '')

# Data Below

LOOPS_FOLDER = 'loops/'
COMB_LOOPS_FOLDER = 'combined_loops/'


def get_loop_infos_from_folder():
    loop_infos = []
    for f in os.listdir(LOOPS_FOLDER):
        if not f.endswith('.mp3'):
            continue
        parts = f.split('_')
        parts[-1] = parts[-1].split('.')[0]
        loop_infos.append({
            'name': parts[0],
            'tempo': parts[1],
            'key': parts[2],
        })
    return loop_infos

def get_comb_loop_infos_from_folder():
    loop_infos = []
    for f in os.listdir(COMB_LOOPS_FOLDER):
        if not f.endswith('.mp3'):
            continue
        parts = f.split('_')
        parts[-1] = parts[-1].split('.')[0]
        loop_infos.append({
            'name': parts[0],
            'tempo': parts[1],
            'key': parts[2],
        })
    return loop_infos
