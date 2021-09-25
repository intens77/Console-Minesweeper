import game
from os.path import exists
from zipfile import ZipFile
import shutil
from pathlib import Path

def check_result(win_flag):
    game.display_field_state()
    if win_flag:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. Don't despair and try again!")
    game.restart_game()


def save_game_state(field):
    if Path("saved_results.zip"):
        with ZipFile('saved_results.zip', 'w') as myzip:
            file_index = str(len(myzip.infolist()) + 1)
            file = open("file_{0}.txt".format(file_index), "w+")
            for row in field:
                for symbol in row:
                    file.write("{0}".format(symbol))
                file.write('\n')
            file.close()
            #myzip.write("file_{0}.txt".format(file_index))
            shutil.move("file_{0}.txt".format(file_index), "saved_results.zip")
            myzip.close()
    else:
        with ZipFile('saved_results.zip', 'w') as myzip:
            file = open("file_1.txt", "w+")
            for row in field:
                for symbol in row:
                    file.write("{0}".format(symbol))
                file.write('\n')
            file.close()
            shutil.move("file_1.txt", "saved_results.zip")
            myzip.close()
