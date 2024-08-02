from tkinter import *

def button_clicked():
    print("You clicked on the button!")
root = Tk() #creates a window
root.geometry('720x488') #gives dimension of the output window in the form widthxheight

title = Label(root, text='Hii. I am learning GUI', bg = '#FBDAFF', fg='#DF3D63', font=('Gabriella', 32))
title.pack()

btn = Button(root, text='Click Me', font=('', 26), command=button_clicked) #creates a button: Button(which window you want button, what text you want)
btn.pack(side=TOP) #dynamic layout to show widgets
root.mainloop() #loops the window until we close - all our actions have to be written between root = Tk() and this line. 


