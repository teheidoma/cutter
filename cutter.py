import ffmpeg
import sys
import os
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    if len(sys.argv) == 4:
        stream = ffmpeg.input(sys.argv[3], ss=sys.argv[1], to=sys.argv[2])
        stream = ffmpeg.output(stream, find_name(sys.argv[3]))
        ffmpeg.run(stream, overwrite_output=True)

def tomp3():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        mp3_path = re.sub(r'\.[^.]+$', '.mp3', path)
        stream = ffmpeg.input(path)
        stream = ffmpeg.output(stream, find_name(mp3_path))
        ffmpeg.run(stream, overwrite_output=True)

def find_name(path: str):
    counter = 0
    while True:
        if counter > 0:
            new_path = path.replace('.mp3', f'.cut{counter}.mp3').replace('.mp4', f'.cut{counter}.mp4')
        else:
            new_path = path.replace('.mp3', '.cut.mp3').replace('.mp4', '.cut.mp4')
        counter += 1
        print(new_path)
        if not os.path.exists(new_path):
            return new_path


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
