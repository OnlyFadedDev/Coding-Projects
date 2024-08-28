import PyPDF2
import sys


# Small Script to turn a page using file reading 
'''
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(page.rotateCounterClockwise(90))
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
'''

# Will combine as many pdf's you give it into one and name it super.pdf

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')




