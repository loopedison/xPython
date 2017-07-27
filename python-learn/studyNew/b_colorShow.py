#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
import tkinter.filedialog

colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

root = tkinter.Tk()
f = tkinter.Frame(root, height=200, width=200)
f.color = 0
f['bg'] = colors[f.color]
def foo():
    f.color = (f.color+1)%(len(colors))
    f['bg'] = colors[f.color]
    f.after(500, foo)
f.pack()
f.after(500, foo)

f.mainloop()
