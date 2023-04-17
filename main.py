##############################DSA Final Project################################
#######################Sorting ALgorithms Visualizer######################


from tkinter import *
from tkinter import ttk
import random
from colors import *

#------------------------------ Importing algorithms-----------------------------
from algorithms.mergeSort import merge_sort
from algorithms.selectionSort import selection_sort
from algorithms.bubbleSort import bubble_sort
from algorithms.quickSort import quick_sort
from algorithms.insertionSort import insertion_sort

#-----------------------------Main screen----------------------------------------
screen = Tk()
screen.title("DSA Sorting Algorithms Visualizer")
screen.maxsize(1000, 800)
screen.config(bg = 'black')
# welcome = ttk.Label(text="Hello")
# welcome.pack()

info = []
select_spd = StringVar()
name_algo = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']
algo_list = ['Merge Sort','Selection Sort', 'Quick Sort', 'Bubble Sort','Insertion Sort' ]

def sort():
    global info
    timeTick = set_speed()
    
    if algo_menu.get() == 'Insertion Sort':
        insertion_sort(info, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(info, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(info, 0, len(info)-1, drawData, timeTick)
    elif algo_menu.get() == 'Bubble Sort':
        bubble_sort(info, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(info, 0, len(info)-1, drawData, timeTick)


def set_speed():
    if speed_menu.get()=='Fast':
        return 0.001
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.3

#--------This Function would be used to to draw numerical arrays+ as bars ---------------------

def drawData(info, colorArray):
    canvas.delete("all")
    gap_between = 5
    height_canva = 400
    left_space = 5
    Width_canva = 800
    width = Width_canva / (len(info) + 1)
    normalizedData = [i / max(info) for i in info]

    for i, height in enumerate(normalizedData):
        axis_yone = height_canva
        axis_xone = (i + 1) * width + left_space
        axis_yzero = height_canva - height * 390
        axis_xzero = i * width + left_space + gap_between
        canvas.create_rectangle(axis_xzero, axis_yzero, axis_xone, axis_yone, fill=colorArray[i])

    screen.update_idletasks()

#-------------------------- generate would generate random arrays----------------------

def generate():
    global info

    info = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        info.append(random_value)

    drawData(info, [BLACK for x in range(len(info))])

#---------------------------------- UI -----------------------------------------
Screen_UserInterface = Frame(screen, width= 900, height=300, bg='black')
Screen_UserInterface.grid(row=0, column=0, padx=10, pady=5)

Second_label = Label(Screen_UserInterface, text="Sorting Speed: ", bg='grey')
Second_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
speed_menu = ttk.Combobox(Screen_UserInterface, textvariable=select_spd, values=speed_list)
speed_menu.grid(row=1, column=1, padx=10, pady=10)
speed_menu.current(0)

First_label = Label(Screen_UserInterface, text="Please Select An Algorithm: ", bg='grey')
First_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(Screen_UserInterface, textvariable=name_algo, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

canvas = Canvas(screen, width=800, height=400, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=10)

second_button = Button(Screen_UserInterface, text="Generate Array", command=generate, bg=LIGHT_GRAY)
second_button.grid(row=2, column=0, padx=0, pady=5)

first_button= Button(Screen_UserInterface, text="Sort", command=sort, bg=LIGHT_GRAY)
first_button.grid(row=2, column=1, padx=5, pady=5)




screen.mainloop()
