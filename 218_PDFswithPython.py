import PyPDF2 

with open('dummy.pdf', 'rb') as file:
    #print(file)
    #<_io.TextIOWrapper name='dummy.pdf' mode='r' encoding='cp1252'>

    reader = PyPDF2.PdfFileReader(file)
    #print(reader.numPages) 
    #PdfReadWarning: PdfFileReader stream/file object is not in binary mode. It may not be read correctly. [pdf.py:1079]
    #solve by changing "with open('dummy.pdf', 'r') as file:" to "with open('dummy.pdf', 'rb') as file:"
    #correct ouput = 1
    
    pageToRotate = reader.getPage(0)
    #print(pageToRotate) # value = 0 refer to the first page
    # {'/Type': '/Page', '/Parent': IndirectObject(4, 0), '/Resources': IndirectObject(11, 0), '/MediaBox': [0, 0, 595, 842], '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': <PyPDF2.generic.BooleanObject object at 0x0000021209CE6AF0>}, '/Contents': IndirectObject(2, 0)}

    print(pageToRotate.rotateClockwise(90))
    #{'/Type': '/Page', '/Parent': IndirectObject(4, 0), '/Resources': IndirectObject(11, 0), '/MediaBox': [0, 0, 595, 842], '/Group': {'/S': '/Transparency', '/CS': '/DeviceRGB', '/I': <PyPDF2.generic.BooleanObject object at 0x0000021209CE6AF0>}, '/Contents': IndirectObject(2, 0), '/Rotate': 90}

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(pageToRotate)            
    with open('tilt.pdf', 'wb') as new_file: #write in binary format
        writer.write(new_file) #returns a corrupted file if this code "writer.addPage(pageToRotate)" is missing. 
        #with writer.addPage(pageToRotate) added before saving as binary file "tilt.pdf", the output is a rotated PDF

