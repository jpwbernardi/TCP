#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import _thread
from client import processOrder

class Application():
    def __init__(self):
        self.gui = tk.Tk()
        self.pathtxt = tk.StringVar()
        self.porttxt = tk.StringVar()
        self.addrtxt = tk.StringVar()
        self.sttstxt = tk.StringVar()
        self.cwidgets()
        self.gui.wm_title("Client")
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
        self.submit["command"] = self.prep
        self.submit.pack()

        self.lstts = tk.Label(self.gui, textvariable = self.sttstxt)
        self.lstts.pack()

    def searchfile(self):
        path = filedialog.askopenfilename()
        if (path != ""):
            self.pathtxt.set(path)

    def prep(self):
        self.sttstxt.set("Processing...")
        self.entry('disabled');
        _thread.start_new_thread(self.sendtoserv, ())

    def sendtoserv(self):
        try:
            tk.messagebox.showinfo('Result', processOrder(self.addrtxt.get(), int(self.porttxt.get()), self.pathtxt.get()))
        except ValueError:
            tk.messagebox.showerror('Error', 'Port must be an iteger')
        finally:
            self.entry('normal')
            self.sttstxt.set("")

    def entry(self, status):
        self.search.config(state = status)
        self.submit.config(state = status)
        self.addr.config(state = status)
        self.port.config(state = status)
        if (status == 'normal'):
            status = 'readonly'
        self.path.config(state = status)

    def on_closing(self):
        self.gui.destroy()

    def run(self):
        self.gui.mainloop()


def main():
    Application().run()

if __name__ == "__main__":
    main()
