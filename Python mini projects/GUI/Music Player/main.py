from tkinter import *
from style import *
import os
import random
import time

def get_music():
    files = os.listdir('Python mini projects\GUI\Music Player\music_files')
    return files

def run_music():
    while True:
        music = get_music()
        play = random.choice(music)
        play_path = os.path.join(os.curdir, 'Python mini projects\GUI\Music Player\music_files', play)
        os.startfile(play_path)
        print(play_path)
        time.sleep(15)

root = Tk()
root.configure(bg=pink)
root.geometry('480x320')

title = Label(root, text="Music Program", fg = fgcolor, bg = pink, font=(fonttype, 28))
title.pack()
body_text = Label(root, text="This program plays random song when you press the button", fg = fgcolor, bg = pink, font=(fonttype, 20))
body_text.pack()


btn = Button(root, text="Click Button", fg = '#000000', bg = '#DFDFDF', font=(fonttype, 24), command=run_music)
btn.pack(side=BOTTOM)
root.mainloop()

