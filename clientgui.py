#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog

class Application():
    def __init__(self):
        self.gui = tk.Tk()
        self.pathtxt = tk.StringVar()
        self.porttxt = tk.StringVar()
        self.addrtxt = tk.StringVar()
        self.cwidgets()
        self.gui.protocol("WM_DELETE_WINDOW", self.on_closing)

    def cwidgets(self):
        self.laddr = tk.Label(self.gui, text="Server address")
        self.addr = tk.Entry(self.gui, exportselection=0, textvariable=self.addrtxt)
        self.laddr.pack(); self.addr.pack(fill='x')
        self.lport = tk.Label(self.gui, text="Port")
        self.port = tk.Entry(self.gui, exportselection=0, textvariable=self.porttxt)
        self.lport.pack(); self.port.pack(fill='x')
        self.fileselframe = tk.Frame(self.gui)
        self.lpath = tk.Label(self.fileselframe, text="File path")
        self.path = tk.Entry(self.fileselframe, exportselection=0, state='readonly', textvariable=self.pathtxt)
        self.lpath.pack(); self.path.pack(fill='x', side='left', expand=1)
        self.search = tk.Button(self.fileselframe)
        self.search["text"] = "Search"
        self.search["command"] = self.searchfile
        self.search.pack(side='right');
        self.fileselframe.pack(fill='x')
        self.submit = tk.Button(self.gui)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.sendtoserv
        self.submit.pack()

    def searchfile(self):
        path = filedialog.askopenfilename()
        if (path != ""):
            self.pathtxt.set(path)

    def sendtoserv(self):
        print("{}\n{}\n{}".format(self.addrtxt.get(), self.porttxt.get(), self.pathtxt.get()));

    def on_closing(self):
        self.gui.destroy()

    def start(self):
        self.gui.mainloop()

app = Application()
app.start()
