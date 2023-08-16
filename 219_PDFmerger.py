#to run, in the command prompt, call the py file, and indicate the all the pdf files to merge

import sys
import PyPDF2

# Get the list of PDFs to merge (minimum 1 file; no max)
inputs = sys.argv[1:]

# From the resulting list, loop through all the PDFs 
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('resulting_merged.pdf')
    
    #count the number of resulting merged file by initially assigning the result to "reader", then use numPages
    reader = PyPDF2.PdfFileReader('resulting_merged.pdf') 
    print(reader.numPages)


pdf_combiner(inputs) #run in the commandprompt:



# C:\Users\GayCalaranan.000\Documents\Programming\Udemy - Python - ZTM>python 219_PDFmerger.py dummy.pdf twopage.pdf tilt.pdf
#output:
# dummy.pdf
# twopage.pdf
# tilt.pdf

# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('tilt2.pdf', 'wb') as new_file:
#         writer.write(new_file)

