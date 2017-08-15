#!/usr/bin/env python
#coding=utf-8

import tkinter
from tkinter import messagebox

# String vars for texts
text_button = "boton"
text_dialog_title = "Salir"
text_dialog_msg = "Desea cerrar el programa?"
#El seba se la come atravesá#

# Functions
def button_click():
    # Button action
    exit_response = messagebox.askyesno(text_dialog_title, text_dialog_msg)
    if exit_response == True:
        exit(0)

# Window config
main_window = tkinter.Tk()
main_window.geometry("800x500")
main_window.title("package manager")


# Button
button = tkinter.Button(text=text_button, command=button_click)



# Set button into window
button.pack()
# Show window
main_window.mainloop()
