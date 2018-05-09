#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk

def pushed(self):
    self["text"] = "押されました"

# create a main window
root = tk.Tk()

# change the title
root.title("simple gui")

# change the window size to 320 x 240
root.geometry("320x240")

# add a label
label = tk.Label(root, text="Hello")
label.grid()

# add a button
button = tk.Button(root, text="ボタン", command=lambda : pushed(button))
button.grid()

# display the root
root.mainloop()
