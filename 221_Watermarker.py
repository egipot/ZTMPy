import PyPDF2

template = PyPDF2.PdfFileReader(open('resulting_merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))

output = PyPDF2.PdfFileWriter()

#loop according to the number of pages in the template
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0)) #get the watermark which is in one-page only
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)

        
