from tkinter import *

counter = 0


def get_counter():
    return int(counter)


def up_counter(counter):
    counter += 1


window = Tk()
window.geometry("720x480")

frame_button = Frame(window, width=20, height=10)
frame_button.pack(expand=YES)
cookie = Button(frame_button,  width=20, height=10, command=up_counter(int(counter)))
cookie.pack()

frame_number = Frame(window)

window.mainloop()
