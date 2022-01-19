from locale import normalize
from textwrap import fill
from tkinter import *
from tkinter import ttk

import random
from algorithms.bubbleSort import bubble_sort
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
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(rand_data)+1)
    offset = 4
    spacing = 2
    normalized_data = [i / max(rand_data) for i in rand_data]

    for i, height in enumerate(normalized_data):
        x0= i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
    
    window.update_idletasks()
    

def generate():
    global data
    data=[]
    for i in range(0, 100):
        random_value = random.randint(1,150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])
    

def set_speed():
    if speed_combo.get() == "Slow":
        return 0.3

    elif speed_combo.get() == "Medium":
        return 0.1

    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()
    bubble_sort(data, drawData, timeTick)
    pass

frame = Frame(window, width=900, height=300, bg=WHITE)
frame.grid(row=0, column=0, padx=10, pady=5)

label_1 = Label(frame, text="Algos", bg=WHITE)
label_1.grid(row=0, column=0, padx=10, pady=5, sticky=W)

algo_combo = ttk.Combobox(frame, textvariable=algo_name, values=algo_list)
algo_combo.grid(row=0, column=1, padx=5, pady=5)
algo_combo.current(0)

label_2 = Label(frame, text="Sorting Speed", bg=WHITE)
label_2.grid(row=1, column=0, padx=10, pady=5, sticky=W)

speed_combo = ttk.Combobox(frame, textvariable=speed_name, values=speed_list)
speed_combo.grid(row=1, column=1, padx=5, pady=5)
speed_combo.current(0)

button_1 = Button(frame, text="Sort", command=sort, bg=LIGHT_GRAY)
button_1.grid(row=2, column=1, padx=5,pady=5)

button_2 = Button(frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
button_2.grid(row=2, column=0, padx=5,pady=5)

canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()