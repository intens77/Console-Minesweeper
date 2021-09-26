import os.path
import time
import zipfile

import game
from zipfile import ZipFile


def check_result(win_flag, opened_cells_count):
    game.display_field_state()
    if win_flag:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost. Don't despair and try again!")
    print()
    print()
    print("Game results:")
    print("Steps count:  " + str(opened_cells_count))
    print("Time:   ", end=' ')
    print(time.time() - game.start_time)
    print()
    print()
    game.restart_game()


def save_game_state(field):
    if os.path.exists("saved_results.zip"):
        with zipfile.ZipFile("saved_results.zip", mode='a',
                             compression=zipfile.ZIP_DEFLATED) as archive:
            file_index = str(len(archive.infolist()) + 1)
            file = open("file_{0}.txt".format(file_index), "w+")
            for row in field:
                for symbol in row:
                    file.write("{0}".format(symbol))
                file.write('\n')
            file.close()
            archive.write("file_{0}.txt".format(file_index))
            archive.setpassword(b"26092021")
            os.remove("file_{0}.txt".format(file_index))
    else:
        with ZipFile('saved_results.zip', 'w') as archive:
            file = open("file_1.txt", "w+")
            for row in field:
                for symbol in row:
                    file.write("{0}".format(symbol))
                file.write('\n')
            file.close()
            archive.write("file_1.txt")
            os.remove("file_1.txt")
            archive.setpassword(b"26092021")
            archive.close()
