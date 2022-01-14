from tkinter import *
from tkinter import ttk

import random
from colors import *

window = Tk()
window.title("Sorting Algos Visualized")
window.maxsize(1000,1000)
window.config(bg=WHITE)

algo_name = StringVar()
algo_list = ['Bubble Sort', 'Merg Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

rand_data = []

def drawData(rand_data, colorArray):
    pass

def generate():
    pass

def set_speed():
    pass

def sort():
    pass

frame = Frame(window, width=900, height=300, bg=WHITE)
frame.grid(row=0, column=0, padx=10, pady=5)

label_1 = Label(frame, text="Algos", bg=WHITE)
label_1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

algo_combo = ttk.Combobox(frame, textvariable=algo_name, values=algo_list)
algo_combo.grid(row=0, column=1, padx=5, pady=5)
algo_combo.current(0)

speed_combo = ttk.Combobox(frame, textvariable=algo_name, values=algo_list)




window.mainloop()