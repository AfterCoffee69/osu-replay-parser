import os
import webbrowser
from osrparse import Replay, parse_replay_data
from datetime import datetime


def accuracy_counter(replay_data):
     
     acc = ((300*replay_data.count_300 + 100*replay_data.count_100 + 50*replay_data.count_50) / (300 * (replay_data.count_300 + replay_data.count_100 + replay_data.count_50 + replay_data.count_miss))) * 100

     return acc

def current_datetime():

    now = datetime.now()

    dt = now.strftime("%d_%m_%Y__%H_%M_%S")
    
    return dt

def parser_folder(path):
    files = os.listdir(path)

    dt = current_datetime()

    for file in files:
        file_name, file_extention = os.path.splitext(file)

        if file_extention == ".osr":

            replay_data = Replay.from_path(f"{path}/{file}")

            acc = accuracy_counter(replay_data)

            write_data(dt, replay_data, file_name, acc)


def parser_file(path):

    file_name, file_extention = os.path.splitext(path)
    dir, title = os.path.split(path)
    
    if file_extention == ".osr":
            
            replay_data = Replay.from_path(path)

            acc = accuracy_counter(replay_data)

            write_data(current_datetime(), replay_data, title, acc)
    

def write_data(current_datetime, r, title, acc):

    str = '-' * len(title)

    path = f"stats/{current_datetime}.txt"

    f = open(path, 'a')

    f.write(f'{str}\n{title}\n{str}')
    f.write(f"\nScore - {r.score}\nMax combo - {r.max_combo}\n300 - {r.count_300}\n100 - {r.count_100}\n50 - {r.count_50}\nX - {r.count_miss}\nAcc - {round(acc, 2)}%\n\n\n")

    f.close()

    webbrowser.open('file://' + os.path.realpath(path))



