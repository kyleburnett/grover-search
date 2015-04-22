#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import numpy as np

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

class App(object):
    def __init__(self, master):
        self.master = master

        # Title
        self.master.wm_title("Grover Search")

        # Plot
        self.figure = Figure(figsize=(5,4), dpi=100)
        self.ax = self.figure.add_subplot(111,aspect='equal')

        # self.ax.plot([], [])

        arr = np.array([
            [0,0,1,0],
            [0,0,0,1]
        ])
        X,Y,U,V = zip(*arr)
        self.ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1, color='rgb')

        self.ax.set_xlim([-1.2, 1.2])
        self.ax.set_ylim([-1.2, 1.2])
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_color('none')
        self.ax.get_xaxis().set_ticks([])
        self.ax.get_yaxis().set_ticks([])

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        # Buttons
        self.quit_button = Tk.Button(master=self.master, text='Quit', command=self._quit)
        self.quit_button.pack(side=Tk.RIGHT)
        self.step_button = Tk.Button(master=self.master, text='Step', command=self._step)
        self.step_button.pack(side=Tk.RIGHT)
        self.reset_button = Tk.Button(master=self.master, text='Reset', command=self._reset)
        self.reset_button.pack(side=Tk.RIGHT)
        self.entry_s = Tk.Spinbox(master=self.master)
        self.entry_s.pack(side=Tk.RIGHT)
        self.label_s = Tk.Label(master=self.master, text='  s:')
        self.label_s.pack(side=Tk.RIGHT)
        self.entry_N = Tk.Spinbox(master=self.master)
        self.entry_N.pack(side=Tk.RIGHT)
        self.label_N = Tk.Label(master=self.master, text='  N:')
        self.label_N.pack(side=Tk.RIGHT)

    def _quit(self):
        self.master.quit()
        self.master.destroy()

    def _step(self):
        print('Step')

    def _reset(self):
        # self.ax.clear()
        # a_2 = self.figure.add_subplot(111)
        # t_2 = arange(0.0,3.0,0.01)
        # s_2 = cos(2*pi*t_2)

        # a_2.plot(t_2,s_2)
        # self.ax = a_2
        # self.canvas.draw()
        print('Reset')

def main():
    root = Tk.Tk()
    app = App(root)
    Tk.mainloop()

if __name__ == '__main__':
    main()