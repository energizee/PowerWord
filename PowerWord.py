# PowerWord, an open souce text editor
# Made by ShinyMemesYT

from tkinter import *
import pkinter as pk
from tkinter import ttk
import tkinter as tk
import time
import os

def write_text(text_to_print):
    text.insert(INSERT, text_to_print)

def load():
    text.delete('1.0', END)
    filename = os.path.join(fileDir, 'PowerWordProjects/' + fileloadentry.get() + '') 
    filecontent = open(filename, "r")
    filecontent = filecontent.read()
    write_text(filecontent)
    print(filename)

def save():
    newfilecontent = text.get("1.0",'end-1c')
    print(newfilecontent)
    newfilepath = 'PowerWordProjects/'
    newfilename = os.path.join(newfilepath, savenameentry.get())
    newfile = open(newfilename, 'w+')
    newfile.write(newfilecontent)
    newfile.close()
    write_text("\nSaved to PowerWordProjects.")

def clear():
    text.delete('1.0', END)

fileDir = os.path.dirname(os.path.realpath('__file__'))
print(fileDir)

# Main window
root = Tk()
root.wm_title("PowerWord")
my_image = PhotoImage(master = root,
                      file = "powerwordlogo.png")

logolabel = Label(root,
                  image = my_image)

logolabel.pack()

creditlabel = Label(root,
                    #text = 'An open source text editor, made by ShinyMemesYT.',
                    text = 'An open source code editor, and plain text editor in the one app.',
                    font = ('Ariel',15))

creditlabel.pack()

loadlabel = Label(root,
                    text = 'Load',
                  font = ('Ariel',30))

loadlabel.pack()

fileloadentry = Entry(root)
fileloadentry.pack()

text = Text(root, height=18)
scrollbar = ttk.Scrollbar(root)
linenumbers = pk.LineNumbers(root, text, scrollbar)

write_text("Empty text file. Clear this then you can write your own text then save it!")

loadbutton = Button(root, text="Load", width=10, height=1, command=load)

loadbutton.pack()

newlabel = Label(root,
                   text = 'New',
                   font = ('Ariel',30))

newlabel.pack()

savenamelabel = Label(root, text="Name for the new file(remember the extension):")
savenamelabel.pack()

savenameentry = Entry(root)
savenameentry.pack()

savebutton = Button(root, width=20, height=1, text="Save", command=save)

savebutton.pack()

clearbutton = Button(root, text="Clear", width=20, height=1, command=clear)

clearbutton.pack()

linenumbers.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")
text.pack(side="right", fill="both")

root.mainloop()
