from tkinter import *
from style import *

root = Tk()

root.geometry('420x720')
frame1 = Frame(root, bg = '#9C9CFF')
frame1.pack(side=TOP, expand='YES', fill=BOTH)

frame2 = Frame(root, bg = '#000000')
frame2.pack(side=BOTTOM, expand='YES', fill=BOTH)

result = Label(frame1, text="Rajavi's Calculator\n", **result)
result.pack()

btn_num = Button(frame2, text='', **number)
btn_num.grid(row=0, column=0)
num = list(range(1,10,1))
for i in range(0,3):
    for j in range(0,3):
        btn_num = Button(frame2, text=3*i + j + 1, **number)
        btn_num.grid(row=i+1, column=j)
btn_num = Button(frame2, text=0, **number)
btn_num.grid(row=4, column=1)
add = Button(frame2, text='+', **number)
add.grid(row=1, column=3)
sub = Button(frame2, text='-', **number)
sub.grid(row=2, column=3)
mul = Button(frame2, text='*', **number)
mul.grid(row=3, column=3)
div = Button(frame2, text='/', **number)
div.grid(row=4, column=3)
per = Button(frame2, text='%', **number)
per.grid(row=4, column=2)
eq = Button(frame2, text='=', **number)
eq.grid(row=0, column=3)
ce = Button(frame2, text='CE', **number)
ce.grid(row=0, column=1)


def result_update(button):
    current = str(result.cget('text'))
    updated_text = current + str(button.cget('text'))
    result.configure(text=updated_text)
    #print(updated_text)

for widget in frame2.winfo_children(): #winfo_children gives info of all the widgets in the frame
    widget_text = widget.cget('text')
    #print(type(widget_text))
    if widget_text in [1,2,3,4,5,6,7,8,9,0] or widget_text in ['+', '-', '*', '/', '%']: 
        widget.configure(command=lambda widget=widget: result_update(widget))


def clean():
    result.configure(text="Rajavi's Calculator\n")
ce.configure(command=clean)

def calculate():
    data1 = result.cget('text')
    data = data1.removeprefix("Rajavi's Calculator\n")
    ans = None
    if '/' in data:
        first, second = map(str.strip, data.split('/'))
        ans = int(first) / int(second)
    elif '*' in data:
        first, second = map(str.strip, data.split('*'))
        ans = int(first) * int(second)
    elif '+' in data:
        first, second = map(str.strip, data.split('+'))
        ans = int(first) + int(second)
    elif '-' in data:
        first, second = map(str.strip, data.split('-'))
        ans = int(first) - int(second)
    elif "%" in data:
        first, second = map(str.strip, data.split('%'))
        ans = (int(first) / int(second)) * 100
    result.configure(text = f"Rajavi's Calculator\n{ans}")

eq.configure(command=calculate)

root.mainloop()
