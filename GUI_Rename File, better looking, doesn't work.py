try:
    #python2 imports
    from Tkinter import Tk, Button, Label, N, W, E, S, StringVar, IntVar, ttk, Frame, Entry
    from Tkinter.filedialog import askopenfile
    import os, os.path, glob
    from PyPDF2 import PdfFileWriter, PdfFileReader
except ImportError:
    #python3 imports
    from tkinter import Tk, Button, Label, N, W, E, S, StringVar, IntVar, ttk, Frame, Entry
    from tkinter.filedialog import askopenfile
    import os, os.path, glob
    from PyPDF2 import PdfFileWriter, PdfFileReader

#Select file function
def load_file():
    filename = askopenfile(initialdir="~")
    target_file.set(filename)
    os.chdir(filename)
    print (os.getcwd())

def rename_file(self, event=None, value=None):
    if value is None:
        value = self.get()
    if self.command is not None:
        if value == self.old_value:
            return
        self.command(value)
        self.old_value = value
    self.select_all()

def set(self, text=None, run=False):
    if text is None:
        text = ""
    self.delete(0, tk. END)
    self.insert(0, str(text))
    if run:
        self.input_change(text)
    self.old_value = text
    
self = Tk()
self.minsize(450,100)
self.title("Renamer")

mainframe = ttk.Frame(self, padding="5 5 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

target_file = StringVar()
target_file.set("")

address = StringVar()
page1 = StringVar()

ttk.Button(self, text="Select PDF", command=load_file).grid(column=1, row=1)
ttk.Label(self, textvariable=target_file).grid(column=2, row=1)

ttk.Label(self, text='Addresses: (use comma to separate multiple)').grid(column=1, row=3, sticky=E)
name_box = Entry(self, width=50, textvariable=address)
name_box.grid(column=2, row=3, sticky=W, padx=10)

ttk.Label(self, text='Pages: (use comma to separate multiple)').grid(column=1, row=4, sticky=E)
name_box = Entry(self, width=50, textvariable=page1)
name_box.grid(column=2, row=4, sticky=W, padx=10)

ttk.Label(self).grid(column=1, row=7)
ttk.Button(self, text="Rename", command=rename_file).grid(column=1, row=7)
ttk.Button(self, text="Cancel", command=quit).grid(column=2, row=7, sticky=W)

self.mainloop()
