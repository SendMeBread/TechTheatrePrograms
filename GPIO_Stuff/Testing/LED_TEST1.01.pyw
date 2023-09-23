import RPi.GPIO as GPIO
from tkinter import *

r = 17
g = 18
y = 22
b = 23
o = 26
w = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(g, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(y, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(b, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(o, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(w, GPIO.OUT)

win = Tk()
win.title("LED Off/On")
win.attributes("-fullscreen", True)
win["bg"] = "black"

label = Label(win, text="LED Selection")
label["foreground"] = "white"
label.grid(row=0)

def commit():
    change_list = [r_check.get(), g_check.get(), y_check.get(), b_check.get(), o_check.get(), w_check.get()]
    for c in change_list:
        if c == 1:
            if c == change_list[0]:
                GPIO.output(r, True)
            elif c == change_list[1]:
                GPIO.output(g, True)
            elif c == change_list[2]:
                GPIO.output(y, True)
            elif c == change_list[3]:
                GPIO.output(b, True)
            elif c == change_list[4]:
                GPIO.output(o, True)
            elif c == change_list[5]:
                GPIO.output(w, True)
        elif c == 0:
            if c == change_list[0]:
                GPIO.output(r, False)
            elif c == change_list[1]:
                GPIO.output(g, False)
            elif c == change_list[2]:
                GPIO.output(y, False)
            elif c == change_list[3]:
                GPIO.output(b, False)
            elif c == change_list[4]:
                GPIO.output(o, False)
            elif c == change_list[5]:
                GPIO.output(w, False)
    

r_check = IntVar()
Checkbutton(win, text="RED Off/On", variable=r_check, bg="red", foreground="black").grid(row=1, sticky="nwes")

g_check = IntVar()
Checkbutton(win, text="GREEN Off/On", variable=g_check, bg="green", foreground="black").grid(row=2, sticky="nwes")

y_check = IntVar()
Checkbutton(win, text="YELLOW Off/On", variable=y_check, bg="yellow", foreground="black").grid(row=3, sticky="nwes")

b_check = IntVar()
Checkbutton(win, text="BLUE Off/On", variable=b_check, bg="blue", foreground="black").grid(row=4, sticky="nwes")

o_check = IntVar()
Checkbutton(win, text="ORANGE Off/On", variable=o_check, bg="orange", foreground="black").grid(row=5, sticky="nwes")

w_check = IntVar()
Checkbutton(win, text="WHITE Off/On", variable=w_check, bg="white", foreground="black").grid(row=6, sticky="nwes")

Button(win, text="Commit", command=commit()).grid(row=7, sticky="nwes")

win.mainloop()