import PyPDF2, os

'''
Reading PDF
'''

os.getcwd()
os.chdir(r'C:\Users\Udemy\AutomatingBoringPython\Excel-Word-PDF')

pdfFile = open('soul-of-anime.pdf', 'rb') # Since pdf are binary file, we need to do read binary mode 'rb'
reader = PyPDF2.PdfFileReader(pdfFile) #return a new pdf reader object

reader.numPages #How mnay page is in this pdf

page = reader.getPage(0) #return page object

page.extractText() #extract text from page 0 and return as python string

for page in range(reader.numPages): #printing out all the pages in the pdf
    print(reader.getPage(page).extractText())

'''
Editing PDF
This is very limited and cannot edit individual text or color in pdf due to complex layout
'''

#Adding two PDF files togther into one new pdf
pdfFile2 = open('AMFAQ.pdf', 'rb') #my 2nd PDF file
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter() #Creating new PDF file

for page in range(reader.numPages):
    page = reader.getPage(page)
    writer.addPage(page) #adding the current page to the new writer pdf object

for page in range(reader2.numPages):
    page = reader2.getPage(page)
    writer.addPage(page) #adding the current page to the new writer pdf object

outputFile = open('combinedPDF.pdf', 'wb') #write binary mode
writer.write(outputFile)
outputFile.close()
pdfFile.close()
pdfFile2.close()
