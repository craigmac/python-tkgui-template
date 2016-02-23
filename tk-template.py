#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
Tk GUI template for Python 2.7.x (not 3.x)

:author: "Craig MacEachern"
:email: "craigmaceachern@fastmail.com"
"""

# Python 2/3 Tk compatibility
try:
    import Tkinter as tk
    import ScrolledText as tkst
    import ttk
    import tkFileDialog as tkfd
    import tkMessageBox as tkmb
    import Tix as tix
except ImportError:  # We are on Python 3+
    import tkinter as tk
    import tkinter.scrolledtext as tkst
    import tkinter.filedialog as tkfd
    import tkinter.messagebox as tkmb
    import tkinter.ttk as ttk
    import tkinter.tix as tix


class Application(ttk.Frame):  # Tkinter.Frame goes inside a Tkinter.Tk window
    """Tk Frame that holds GUI Widgets, text, etc."""
    def __init__(self, master=None):
        """
        Intializes and instance of a Tk Frame class.

        :param master: Optional. If none is given the instance will create a
        parent window automagically.
        """
        ttk.Frame.__init__(self, master)

        # Layout - self (Frame) position init
        # Sticky -- which sides will this widget stick to if we have extra room
        self.grid(column=0, row=0)
        self.columnconfigure(0, weight=1)  # Take up additional space
        self.rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the Tk widgets to be drawn and positioned in the Frame.
        Uses ttk to make better themed Tk widgets, rather than standard Tk
        widgets.
        """
        pass
        # Examples
        """
        # Button
        self.my_btn = ttk.Button(
                            self,
                            width=10,
                            text="my button",
                            command=self.run_a_funct
                            )
        self.my_btn.grid(column=0, row=1, sticky=W)

        # Entry
        self.entry_value = StringVar()
        self.entry_value.set("Test string")

        self.my_entry = ttk.Entry(
                                 self,
                                 width=50,
                                 textvariable=self.entry_value
                                 )
        self.my_entry.grid(column=0, row=2, sticky=W)
        """


if __name__ == "__main__":
    root = tk.Tk()  # Tkinter.Tk main window
    root.wm_resizable(0, 0)  # Not resizable in either direction

    # Our application
    app = Application(master=root)
    app.master.title("Title goes here")
    app.master.configure(width=640, height=480, padx=5, pady=5)
    app.mainloop()  # Run it
