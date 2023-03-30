from pydub import AudioSegment

from data import loop_filename_from_info, get_loop_infos_from_folder

LOOPS_FOLDER = 'loops/'
COMB_LOOPS_FOLDER = 'combined_loops/'

def combine_loop(l1, l2):
    l1fn = loop_filename_from_info(l1)
    l2fn = loop_filename_from_info(l2)
    new_info = {
        'name': l1['name'] + l2['name'],
        'tempo': l1['tempo'],
        'key': l1['key'],
    }
    newfn = loop_filename_from_info(new_info)
    l1_seg = AudioSegment.from_mp3(LOOPS_FOLDER + l1fn)
    l2_seg = AudioSegment.from_mp3(LOOPS_FOLDER + l2fn)
    # Decrease volum of l2
    l2_seg = l2_seg - 10 # db
    comb_seg = l1_seg.overlay(l2_seg)
    comb_seg.export(COMB_LOOPS_FOLDER + newfn, format='mp3')

def combine_all_loops():
    loop_infos = get_loop_infos_from_folder()
    for i, l1 in enumerate(loop_infos):
        for j in range(i + 1, len(loop_infos)):
            l2 = loop_infos[j]
            if l2['tempo'] == l1['tempo'] and l2['key'] == l1['key']:
                combine_loop(l1, l2)

if __name__ == '__main__':
    combine_all_loops()