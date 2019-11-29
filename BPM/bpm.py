import librosa
import numpy as np
import os

music_suffix = ['.mp3', '.wav']


def get_music_paths():
    root_dir = os.getcwd()
    list_dirs = os.walk(root_dir)
    for root, dirs, files in list_dirs:
        return files


def calculate_music_npm(path):
    path_list = os.path.splitext(path)
    file_name = path_list[0]
    file_ext = path_list[1]
    if file_ext in music_suffix:
        yy, sr = librosa.load(path, sr=None)
        onset_env = librosa.onset.onset_strength(yy, sr=sr, hop_length=512, aggregate=np.median)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
        print('Music:', path, 'Npm:', tempo)

for path in get_music_paths():
    calculate_music_npm(path)
