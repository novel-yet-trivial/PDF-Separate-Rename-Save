from PyPDF2 import PdfFileWriter, PdfFileReader

# Change the file address
inputpdf = PdfFileReader(open(
    "C://Users//username//Desktop//Original File.pdf", "rb"))

# Change properties for all available set prefixes
# Change names for all individual pages in the set
properties = 'itworks1', 'itworks2'  
names = ("page1", "page2", "page3") #"App_SA205"
filename = []

for prefix in properties:
    for suffix in names:
        filename.append("{}_{}.pdf".format(prefix, suffix))

for i, name in enumerate(filename):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open(name, 'wb') as f:
        output.write(f)
