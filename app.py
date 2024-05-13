""" 
    Created on Thu Sept 17 2020

    @author: umairkarel
"""

import random
from tkinter import ttk
from tkinter import messagebox

# pylint: disable=unused-wildcard-import, wildcard-import
from tkinter import *
from sorting_algorithms import *
from constants import WIDTH, HEIGHT, COLOR


root = Tk()
root.title("Sorting Visualized!")

# Variables
selected_algo = StringVar()
data = []


# Functions
def plot_data(data, color_array): # pylint: disable=redefined-outer-name
    """
    Draws the data on the main frame using the provided color array.

    Parameters:
        data (List[int]): The data to be drawn.
        color_array (List[str]): The array of colors corresponding to each data point.

    Returns:
        None
    """
    main_frame.delete("all")
    c_height = main_frame.winfo_height() - 10
    c_width = main_frame.winfo_width()
    x_width = c_width / (len(data) + 1)
    offset = (c_width) / (len(data) * 10)
    spacing = 10

    for i, height in enumerate(data):
        # Top Left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * (c_height - 30)

        # Bottom Right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        main_frame.create_rectangle(x0, y0, x1, y1, fill=color_array[i])

    root.update()


def generate_data():
    """
    Generates a list of random integers between 1 and the specified size, shuffles the list,
    and normalizes the data.
    The normalized data is then passed to the plot_data function to draw the data on the main frame.

    Parameters:
        None

    Returns:
        None
    """
    # pylint: disable=global-statement
    global data

    # minVal = int(min_entry.get())
    # maxVal = int(max_entry.get())
    size = int(size_entry.get())

    data = [i for i in range(1, size)]
    random.shuffle(data)

    # Normalizing data
    data = [i / max(data) for i in data]

    plot_data(data, [COLOR for _ in range(len(data))])


def start_algorithm():
    """
    Starts the selected sorting algorithm on the data.

    This function checks if the data is already sorted. If it is, it returns without doing anything.
    Otherwise, it disables start button and generate button to prevent further changes to the data.

    Parameters:
        None

    Returns:
        None
    """
    # pylint: disable=global-variable-not-assigned
    global data

    if data == sorted(data):
        return

    # Disabling Once ALgo is Started
    start_button["state"] = "disabled"
    generate_button["state"] = "disabled"

    algorithm = ("_").join(algorithm_menu.get().lower().split())
    # pylint: disable=eval-used
    eval(f"{algorithm}(data, plot_data, speed_scale.get())")

    # Enabling the Button again
    start_button["state"] = "normal"
    generate_button["state"] = "normal"


# Main Canvas
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

UI_FRAME = Frame(root, width=WIDTH, height=HEIGHT, bg="grey", bd=10)
UI_FRAME.place(relx=0.5, rely=0, relwidth=0.96, relheight=0.3, anchor="n")

# Menu Row [1]
Label(UI_FRAME, text="Algorithm", bg="grey", font=("Courier", 20)).place(x=0, y=0)

# Algorithm Selection Dropdown
algorithm_menu = ttk.Combobox(
    UI_FRAME,
    textvariable=selected_algo,
    values=[
        "Bubble Sort",
        "Insertion Sort",
        "Selection Sort",
        "Merge Sort",
        "Quick Sort",
        "Heap Sort",
    ],
    font=("Courier", 15),
)
algorithm_menu.place(x=50, y=35, relheight=0.2, relwidth=0.4)
algorithm_menu.current(0)

speed_scale = Scale(
    UI_FRAME,
    from_=0.2,
    to=0.0,
    length=200,
    digits=2,
    resolution=0.0,
    orient=HORIZONTAL,
    label="Select Speed [sec]",
    font=("Courier", 12),
)
speed_scale.place(relx=0.5, rely=0, relheight=0.47, relwidth=0.35)

# Start Button
start_button = Button(
    UI_FRAME, text="Start", command=start_algorithm, bg="#00a915", font=("Courier", 10)
)
start_button.place(relx=0.87, rely=0.1, relwidth=0.13, relheight=0.3)

# Menu Row[2] (Entry Scales)
size_entry = Scale(
    UI_FRAME,
    from_=10,
    to=150,
    resolution=1,
    orient=HORIZONTAL,
    label="Data Size",
    font=("Courier", 12),
)
size_entry.place(relx=0, rely=0.53, relheight=0.47, relwidth=0.25)

min_entry = Scale(
    UI_FRAME,
    from_=0,
    to=10,
    resolution=1,
    orient=HORIZONTAL,
    label="Min Value",
    font=("Courier", 12),
)
min_entry.place(relx=0.30, rely=0.53, relheight=0.47, relwidth=0.25)

max_entry = Scale(
    UI_FRAME,
    from_=10,
    to=100,
    resolution=1,
    orient=HORIZONTAL,
    label="Max Value",
    font=("Courier", 12),
)
max_entry.place(relx=0.6, rely=0.53, relheight=0.47, relwidth=0.25)

# Generate Button
generate_button = Button(
    UI_FRAME,
    text="Generate",
    command=generate_data,
    bg="#2b3636",
    fg="white",
    font=("Courier", 10),
)
generate_button.place(relx=0.87, rely=0.6, relwidth=0.13, relheight=0.3)

main_frame = Canvas(root, bg="#b1aeae")
main_frame.place(relx=0.5, rely=0.31, relwidth=0.98, relheight=0.68, anchor="n")


def on_closing():
    """
    Defines the behavior when the window is closed.

    This function is called when the user tries to close the window.
    Parameters:
        None

    Returns:
        None
    """
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
