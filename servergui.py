#!/usr/bin/python3
import tkinter as tk
import _thread
from tkinter import ttk
from server import clientthread, startserver

class Application():
    def __init__(self):
        self.gui = tk.Tk()
        self.addrtxt = tk.StringVar()
        self.porttxt = tk.StringVar()
        self.sttstxt = tk.StringVar()
        self.disabled = True
        self.cwidgets()
        self.gui.wm_title("Server")
        self.gui.protocol("WM_DELETE_WINDOW", self.on_closing)

    def cwidgets(self):
        self.n = ttk.Notebook(self.gui)
        self.mainf = ttk.Frame(self.n)
        self.n.add(self.mainf, text='Main')
        self.n.pack(fill='both')

        self.laddr = tk.Label(self.mainf, text="Server address")
        self.addr = tk.Entry(self.mainf, exportselection = 0, textvariable=self.addrtxt)
        self.laddr.pack(); self.addr.pack(fill='x')

        self.lport = tk.Label(self.mainf, text = "Port")
        self.port = tk.Entry(self.mainf, exportselection = 0, textvariable=self.porttxt)
        self.lport.pack(); self.port.pack(fill='x')

        tmpframe = tk.Frame(self.mainf)
        self.lstts = tk.Label(tmpframe, text="Status: disabled", fg='red', textvariable=self.sttstxt)
        self.lstts.pack(side='left')

        self.ctrl = tk.Button(tmpframe)
        self.ctrl["text"] = "Start"
        self.ctrl["command"] = self.prep
        self.ctrl.pack()
        tmpframe.pack()


    #Its only for testing...
    def prep(self):
        if self.disabled:
            #self.entry('disabled')
            _thread.start_new_thread(startserver, (self.addrtxt.get(), int(self.porttxt.get())))


    ### end
    def addtab(self):
        f = ttk.Frame(self.n)
        self.n.add(f, text="Nova")
        self.n.pack()

    def on_closing(self):
        self.gui.destroy()


    def run(self):
        self.gui.mainloop()

def main():
    Application().run()

if __name__ == "__main__":
    main()
