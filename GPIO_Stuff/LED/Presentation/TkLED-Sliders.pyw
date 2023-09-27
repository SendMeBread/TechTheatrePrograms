#Import Modules
import RPi.GPIO as GPIO
import tkinter as tk
import atexit
#Create window
root = tk.Tk()
root.attributes("-fullscreen", True)
root['bg'] = "black"
tk.Label(root, text="LED Fun!", fg='white', bg="black").grid(row=0, column=3)
#Setup GPIO Vars
r = 21
g = 7
b = 19
w = 9
#Setup GPIO Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(w, GPIO.OUT)
#Create IntVars
r_var = tk.IntVar()
g_var = tk.IntVar()
b_var = tk.IntVar()
w_var = tk.IntVar()
#RED Functions
def r_add_1():
    global r_var
    r_var.set(r_var.get() + 1)
def r_sub_1():
    global r_var
    r_var.set(r_var.get() - 1)
def r_add_10():
    global r_var
    r_var.set(r_var.get() + 10)
def r_sub_10():
    global r_var
    r_var.set(r_var.get() - 10)
def r_max():
    global r_var
    r_var.set(100)
def r_off():
    global r_var
    r_var.set(0)
def r_trace(var, index, mode):
    rp = GPIO.PWM(r, 50)
    rp.start(0)
    try:
        while 1:
            rp.ChangeDutyCycle(r_var.get())
    except KeyboardInterrupt:
        pass
    return rp
#GREEN Functions
def g_add_1():
    global g_var
    g_var.set(g_var.get() + 1)
def g_add_10():
    global g_var
    g_var.set(g_var.get() + 10)
def g_sub_1():
    global g_var
    g_var.set(g_var.get() - 1)
def g_sub_10():
    global g_var
    g_var.set(g_var.get() - 10)
def g_max():
    global g_var
    g_var.set(100)
def g_off():
    global g_var
    g_var.set(0)
def g_trace(var, index, mode):
    gp = GPIO.PWM(g, 50)
    gp.start(0)
    try:
        while 1:
            gp.ChangeDutyCycle(g_var)
    except KeyboardInterrupt:
        pass
    return gp
#BLUE Functions
def b_add_1():
    global b_var
    b_var.set(b_var.get() + 1)
def b_add_10():
    global b_var
    b_var.set(b_var.get() + 10)
def b_sub_1():
    global b_var
    g_var.set(b_var.get() - 1)
def b_sub_10():
    global b_var
    b_var.set(b_var.get() - 10)
def b_max():
    global b_var
    g_var.set(100)
def b_off():
    global b_var
    b_var.set(0)
def b_trace(var, index, mode):
    bp = GPIO.PWM(b, 50)
    bp.start(0)
    try:
        while 1:
            bp.ChangeDutyCycle(b_var)
    except KeyboardInterrupt:
        pass
    return bp
#WHITE Functions
def w_add_1():
    global w_var
    w_var.set(w_var.get() + 1)
def w_add_10():
    global w_var
    w_var.set(w_var.get() + 10)
def w_sub_1():
    global w_var
    w_var.set(w_var.get() - 1)
def w_sub_10():
    global w_var
    w_var.set(w_var.get() - 10)
def w_max():
    global w_var
    w_var.set(100)
def w_off():
    global w_var
    w_var.set(0)
def w_trace(var, index, mode):
    wp = GPIO.PWM(w, 50)
    wp.start(0)
    try:
        while 1:
            wp.ChangeDutyCycle(w_var)
    except KeyboardInterrupt:
        pass
    return wp
#Sliders
r_scale = tk.Scale(root, fg="black", variable=r_var, from_= 0, to= 100, orient="horizontal", background="#f00", activebackground="#000").grid(row=1, column=4)
g_scale = tk.Scale(root, fg="black", variable=g_var, from_= 0, to= 100, orient="horizontal", background="#0f0", activebackground="#000").grid(row=2, column=4)
b_scale = tk.Scale(root, fg="black", variable=b_var, from_= 0, to= 100, orient="horizontal", background="#00f", activebackground="#000").grid(row=3, column=4)
w_scale = tk.Scale(root, fg="black", variable=w_var, from_= 0, to= 100, orient="horizontal", background="#fff", activebackground="#000").grid(row=4, column=4)
#RED Buttons
tk.Button(root, width=5, text="OFF", command=r_off, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=1)
tk.Button(root, width=5, text="+10", command=r_add_10, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=6)
tk.Button(root, width=5, text="-1", command=r_sub_1, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=3)
tk.Button(root, width=5, text="-10", command=r_sub_10, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=2)
tk.Button(root, width=5, text="+1", command=r_add_1, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=5)
tk.Button(root, width=5, text="MAX", command=r_max, fg="#000", bg="#f00", borderwidth=0, activebackground="#000", activeforeground="#f00").grid(row=1, column=7)
#GREEN Buttons
tk.Button(root, width=5, text="OFF", command=g_off, fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=1)
tk.Button(root, width=5, text="-10", command=g_add_10, fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=6)
tk.Button(root, width=5, text="-1", command=g_sub_1, fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=3)
tk.Button(root, width=5, text="-10", command=g_sub_10, fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=2)
tk.Button(root, width=5, text="+1", command=g_add_1, fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=5)
tk.Button(root, width=5, text="MAX", command=g_off, fg="#000", bg="#0f0", borderwidth=0, activebackground="#000", activeforeground="#0f0").grid(row=2, column=7)
#BLUE Buttons
tk.Button(root, width=5, text="OFF", command=b_off, fg="#000", bg="#00f", borderwidth=0, activebackground="#000", activeforeground="#00f").grid(row=3, column=1)
tk.Button(root, width=5, text="-10", command=b_add_10, fg="#000", bg="#00f", borderwidth=0, activebackground="#000", activeforeground="#00f").grid(row=3, column=6)
tk.Button(root, width=5, text="-1", command=b_sub_1, fg="#000", bg="#00f", borderwidth=0, activebackground="#000", activeforeground="#00f").grid(row=3, column=3)
tk.Button(root, width=5, text="-10", command=b_sub_10, fg="#000", bg="#00f", borderwidth=0, activebackground="#000", activeforeground="#00f").grid(row=3, column=2)
tk.Button(root, width=5, text="+1", command=b_add_1, fg="#000", bg="#00f", borderwidth=0, activebackground="#000", activeforeground="#00f").grid(row=3, column=5)
tk.Button(root, width=5, text="MAX", command=b_off, fg="#000", bg="#00f", borderwidth=0, activebackground="#000", activeforeground="#00f").grid(row=3, column=7)
#WHITE Buttons
tk.Button(root, width=5, text="OFF", command=w_off, fg="#000", bg="#fff", borderwidth=0, activebackground="#000", activeforeground="#fff").grid(row=4, column=1)
tk.Button(root, width=5, text="-10", command=w_add_10, fg="#000", bg="#fff", borderwidth=0, activebackground="#000", activeforeground="#fff").grid(row=4, column=6)
tk.Button(root, width=5, text="-1", command=w_sub_1, fg="#000", bg="#fff", borderwidth=0, activebackground="#000", activeforeground="#fff").grid(row=4, column=3)
tk.Button(root, width=5, text="-10", command=w_sub_10, fg="#000", bg="#fff", borderwidth=0, activebackground="#000", activeforeground="#fff").grid(row=4, column=2)
tk.Button(root, width=5, text="+1", command=w_add_1, fg="#000", bg="#fff", borderwidth=0, activebackground="#000", activeforeground="#fff").grid(row=4, column=5)
tk.Button(root, width=5, text="MAX", command=w_off, fg="#000", bg="#fff", borderwidth=0, activebackground="#000", activeforeground="#fff").grid(row=4, column=7)
#Column Spacing
root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=0)
root.columnconfigure(4, weight=0)
root.columnconfigure(5, weight=0)
root.columnconfigure(6, weight=0)
root.columnconfigure(7, weight=0)
#Row Spacing
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
#Var Tracers
r_var.trace_add("write", r_trace)
g_var.trace_add("write", g_trace)
b_var.trace_add("write", b_trace)
w_var.trace_add("write", w_trace)
#Initialize Tkinter
tk.mainloop()
#Cleanup GPIOs on exit
def exit_cleanup(r, g, b, w):
    r.stop()
    g.stop()
    b.stop()
    w.stop()
    GPIO.cleanup()
atexit.register(exit_cleanup(r_trace, g_trace, b_trace, w_trace))