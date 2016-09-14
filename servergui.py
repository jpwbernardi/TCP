#!/usr/bin/python3
import tkinter as tk
import thread as thread
from tkinter import ttk
from tkinter import messagebox
from server import clientthread, startserver

class Application():
    def __init__(self):
        self.gui = tk.Tk()
        self.addrtxt = tk.StringVar()
        self.porttxt = tk.StringVar()
        self.sttstxt = tk.StringVar()
        self.server = thread.thread()
        self.cwidgets()
        self.gui.wm_title("Server")
        self.gui.protocol("WM_DELETE_WINDOW", self.on_closing)

    def cwidgets(self):
        self.laddr = tk.Label(self.gui, text="Server address")
        self.addr = tk.Entry(self.gui, exportselection = 0, textvariable=self.addrtxt)
        self.laddr.pack(); self.addr.pack(fill='x')

        self.lport = tk.Label(self.gui, text = "Port")
        self.port = tk.Entry(self.gui, exportselection = 0, textvariable=self.porttxt)
        self.lport.pack(); self.port.pack(fill='x')

        tmpframe = tk.Frame(self.gui)
        self.lstts = tk.Label(tmpframe, text="Status: disabled", fg='red', textvariable=self.sttstxt)
        self.lstts.pack(side='left')

        self.ctrl = tk.Button(tmpframe)
        self.ctrl["text"] = "Start"
        self.ctrl["command"] = self.prep
        self.ctrl.pack()
        tmpframe.pack()


    def prep(self):
        if self.ctrl["text"] == "Start":
            try:
                self.server.run(startserver, self.addrtxt.get(), int(self.porttxt.get()))
            except ValueError:
                tk.messagebox.showerror('Error', 'Port must be an iteger')
                return
            self.ctrl["text"] = "Stop"
        else:
            self.server.stop()
            while not self.server.finished():
                continue
            self.server.reset()
            self.ctrl["text"] = "Start"


    ### end
    def addtab(self):
        f = ttk.Frame(self.n)
        self.n.add(f, text="Nova")
        self.n.pack()

    def on_closing(self):
        self.server.stop()
        self.gui.destroy()


    def run(self):
        self.gui.mainloop()

def main():
    Application().run()

if __name__ == "__main__":
    main()
