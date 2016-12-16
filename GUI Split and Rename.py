from __future__ import print_function

try:
    #python2 imports
    import Tkinter as tk
    from tkFileDialog import askopenfilename
    from tkMessageBox import showerror
except ImportError:
    #python3 imports
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    from tkinter.messagebox import showerror
    #~ from PyPDF2 import PdfFileWriter, PdfFileReader

class AutoSelectEntry(tk.Entry):
    def __init__(self, master, command=None, **kwargs):
        """Entry widget that auto selects when focused
       command is a function or list of functions to execute on value change"""
        tk.Entry.__init__(self, master, **kwargs)
        self.command = command

        self.bind('<FocusIn>', self.select_all)
        self.bind('<Return>', self.input_change)
        self.bind('<FocusOut>', self.input_change)

        self.old_value = None

    def select_all(self, event=None):
        self.selection_range(0, tk.END)

    def input_change(self, event=None, value=None):
        if value is None:
            value = self.get()
        if self.command is not None:
            if value == self.old_value:
                return #check for a change; prevent command trigger when just tabbing through
            self.command(value)
            self.old_value = value
        self.select_all()

    def set(self, text=None, run=False):
        if text is None:
            text = ""
        self.delete(0, tk.END)
        self.insert(0, str(text))
        if run:
            self.input_change(text)
        self.old_value = text

class Browse(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.button = tk.Button(self, text="Browse", command=self.load_file, width=10)
        self.button.grid(row=1, column=0, sticky=tk.W)

    def load_file(self):

        options = {
            'filetypes':(("PDF File", "*.pdf"), ("All files", "*.*")),
            'initialdir': None # code to recall last dir used here.
            }
        self.master.fname = askopenfilename(**options)
        if self.master.fname:
            #loading code here?
            self.master.switch_to_main()
        else:
            print("user cancelled operation")


class MainFrame(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.initialize()

    def initialize(self):

        #Add and associate radio buttons
        fields = [
            "Enter Addresses here.",
            "Enter Page One Name here.",
            "Enter Page Two Name here.",
            "Enter Page Three Name here.",
            "Enter Page Four Name here."]

        self.entries = []
        for row, field in enumerate(fields, start=2):
            entry = AutoSelectEntry(self, command=self.OnPressEnter)
            entry.set(field)
            entry.grid(column=0, row=row, sticky='EW')
            self.entries.append(entry)


        button = tk.Button(self,text=u"Generate File",
                                command=self.OnButtonClick)
        button.grid(column=2,row=1)

        self.labelVariable = tk.StringVar()
        label = tk.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=7,columnspan=3,sticky='EW')
        self.labelVariable.set(u"File Name Example")

    def OnButtonClick(self):
        pass
        #what was this supposed to do?

    def OnPressEnter(self, data):
        self.labelVariable.set(data)


class SimpleApp(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.browse = Browse(self)
        self.browse.pack()

    def switch_to_main(self):
        self.browse.destroy()
        print("User selected", self.fname)
        self.mainframe = MainFrame(self)
        self.mainframe.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    app.pack()
    root.title('my application')
    root.resizable(True,False)
    root.mainloop()
