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

        self._init_axes()

        # Counter
        self.str = Tk.StringVar()
        self.str.set('Iteration count:')
        self.label_count = Tk.Label(master=self.master, textvariable=self.str)
        self.label_count.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        # Entries & Buttons
        self.label_N = Tk.Label(master=self.master, text='  N:')
        self.label_N.pack(side=Tk.LEFT)
        self.entry_N = Tk.Spinbox(master=self.master)
        self.entry_N.pack(side=Tk.LEFT)
        self.label_t = Tk.Label(master=self.master, text='  |t|:')
        self.label_t.pack(side=Tk.LEFT)
        self.entry_t = Tk.Spinbox(master=self.master)
        self.entry_t.pack(side=Tk.LEFT)
        self.reset_button = Tk.Button(master=self.master, text='Reset', command=self._reset)
        self.reset_button.pack(side=Tk.LEFT)
        self.step_button = Tk.Button(master=self.master, text='Step', command=self._step)
        self.step_button.pack(side=Tk.LEFT)
        self.quit_button = Tk.Button(master=self.master, text='Quit', command=self._quit)
        self.quit_button.pack(side=Tk.LEFT)

        # State
        self.state = 0
        self.iteration = 1

    def _init_axes(self):
        self.ax.clear()
        arr = np.array([
            [0,0,1,0],
            [0,0,0,1]
        ])
        X,Y,U,V = zip(*arr)
        self.ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)

        self.ax.set_xlim([-1.2, 1.2])
        self.ax.set_ylim([-1.2, 1.2])
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_color('none')
        self.ax.get_xaxis().set_ticks([])
        self.ax.get_yaxis().set_ticks([])

    def _quit(self):
        self.master.quit()
        self.master.destroy()

    def _step(self):
        self._init_axes()

        if self.state == 0: # The vector |psi> (initial)
            try:
                N = float(self.entry_N.get())
                t = float(self.entry_t.get())
                self.entry_N.configure(state='disabled')
                self.entry_t.configure(state='disabled')
            except ValueError:
                print "Please enter a number"
                return

            self.str.set('Iteration Count: ' + str(self.iteration))
            self.theta = np.arcsin(np.sqrt(t/N))
            x = np.cos(self.theta)
            y = np.sin(self.theta)
            arr = np.array([
                [0,0,x,y]
            ])
            X,Y,U,V = zip(*arr)
            self.quiver = self.ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1,color='rgb')
            self.state = 2
        elif self.state == 1: # Drawing the new vector |psi>
            self.str.set('Iteration Count: ' + str(self.iteration))
            x = np.cos(self.theta)
            y = np.sin(self.theta)
            arr = np.array([
                [0,0,x,y]
            ])
            X,Y,U,V = zip(*arr)
            self.quiver = self.ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1,color='rgb')
            self.state = 2
        elif self.state == 2: # Drawing the vectors |psi>, F|psi>
            x = np.cos(self.theta)
            y = np.sin(self.theta)
            arr = np.array([
                [0,0,x,y],
                [0,0,x,-y]
            ])
            X,Y,U,V = zip(*arr)
            self.quiver = self.ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1,color='rgb')
            self.state = 3
        elif self.state == 3: # Drawing the vectors |psi>, F|psi>, WF|psi>
            x = np.cos(self.theta)
            y = np.sin(self.theta)
            x2 = np.cos(self.theta * 3)
            y2 = np.sin(self.theta * 3)
            arr = np.array([
                [0,0,x,y],
                [0,0,x,-y],
                [0,0,x2,y2]
            ])
            X,Y,U,V = zip(*arr)
            self.quiver = self.ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1,color='rgb')
            self.theta *= 3
            self.state = 1
            self.iteration += 1

        self.canvas.draw()

    def _reset(self):
        self.iteration = 1
        self.entry_N.configure(state='normal')
        self.entry_t.configure(state='normal')
        self.state = 0
        self._init_axes()
        self.canvas.draw()

def main():
    root = Tk.Tk()
    app = App(root)
    Tk.mainloop()

if __name__ == '__main__':
    main()