import RPi.GPIO as GPIO
import tkinter as tk

#Create window
root = tk.Tk()
root.attributes("-fullscreen", True)
root['bg'] = "black"
tk.Label(root, text="LED Fun!", fg='white', bg="black").grid(row=0, column=3)

#Setup GPIOs
r = 17
g = 18
y = 22
b = 23
o = 26
w = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(y, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)
GPIO.setup(o, GPIO.OUT)
GPIO.setup(w, GPIO.OUT)

r_var = tk.IntVar()
g_var = tk.IntVar()
y_var = tk.IntVar()
b_var = tk.IntVar()
o_var = tk.IntVar()
w_var = tk.IntVar()
def r_add():
    global r_var
    r_var.set(r_var.get() + 1)
def r_sub():
    global r_var
    r_var.set(r_var.get() - 1)
def r_max():
    global r_var
    r_var.set(100)
def r_off():
    global r_var
    r_var.set(0)
def r_trace(var, index, mode):
    p = GPIO.PWM(r, 50)
    p.start(0.0)
    try:
        while 1:
            p.ChangeDutyCycle(r_var.get())
    except KeyboardInterrupt:
        pass
    

r_scale = tk.Scale(root, fg="black", variable=r_var, from_=0, to= 100, orient="horizontal", background="#f00", activebackground="#000").grid(row=1, column=2)
g_scale = tk.Scale(root, fg="black", variable=g_var, from_=0, to= 100, orient="horizontal", background="#0f0", activebackground="#000").grid(row=2, column=2)
y_scale = tk.Scale(root, fg="black", variable=y_var, from_=0, to= 100, orient="horizontal", background="#ff0", activebackground="#000").grid(row=3, column=2)
b_scale = tk.Scale(root, fg="black", variable=b_var, from_=0, to= 100, orient="horizontal", background="#00f", activebackground="#000").grid(row=4, column=2)
o_scale = tk.Scale(root, fg="black", variable=o_var, from_=0, to= 100, orient="horizontal", background="#ffa500", activebackground="#000").grid(row=5, column=2)
w_scale = tk.Scale(root, fg="black", variable=w_var, from_=0, to= 100, orient="horizontal", background="#fff", activebackground="#000").grid(row=6, column=2)

#RED Buttons
r_off_b = tk.Button(root, text="OFF", command=r_off, fg="#000", bg="#f00", activebackground="#000", activeforeground="#f00").grid(row=1, column=0)
tk.Button(root, text=u"\u2190", command=r_sub, fg="#000", bg="#f00", activebackground="#000", activeforeground="#f00").grid(row=1, column=1)
tk.Button(root, text=u"\u2192", command=r_add, fg="#000", bg="#f00", activebackground="#000", activeforeground="#f00").grid(row=1, column=3)
tk.Button(root, text="MAX", command=r_max, fg="#000", bg="#f00", activebackground="#000", activeforeground="#f00").grid(row=1, column=4)
#GREEN Buttons
tk.Button(root, text="OFF")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=0)
root.columnconfigure(3, weight=0)
root.columnconfigure(4, weight=1)

tk.mainloop()