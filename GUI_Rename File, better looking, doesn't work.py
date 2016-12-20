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

#Rename function
def rename():
##   i = 0
##   for pdf in os.listdir():
##      file_name, file_extension = os.path.splitext(file)
##      i += 1
##      new_file_name = 'prefix.get(){}.pdf'.format(i)
##      os.rename(file, new_file_name)

    for address in addresses:
        for page in pages:
            filename.append("{}_{}.pdf".format(address, page))

    for i, name in enumerate(filename):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(name, 'wb') as f:
            output.write(f)   

#Build tkinterGUI
self = Tk()
self.minsize(450,100)
self.title("Renamer")

mainframe = ttk.Frame(self, padding="5 5 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

target_file = StringVar()
target_file.set("")

address = StringVar()
page1 = StringVar()
page2 = StringVar()
page3 = StringVar()

ttk.Button(mainframe, text="Select PDF", command=load_file).grid(column=1, row=1)
ttk.Label(mainframe, textvariable=target_file).grid(column=2, row=1)

ttk.Label(mainframe, text='Addresses: (use comma to separate multiple)').grid(column=1, row=3, sticky=E)
name_box = Entry(mainframe, width=50, textvariable=address)
name_box.grid(column=2, row=3, sticky=W, padx=10)

ttk.Label(mainframe, text='Pages: (use comma to separate multiple)').grid(column=1, row=4, sticky=E)
name_box = Entry(mainframe, width=50, textvariable=page1)
name_box.grid(column=2, row=4, sticky=W, padx=10)

ttk.Label(mainframe).grid(column=1, row=7)
ttk.Button(mainframe, text="Rename", command=rename).grid(column=1, row=7)
ttk.Button(mainframe, text="Cancel", command=quit).grid(column=2, row=7, sticky=W)

self.mainloop()
