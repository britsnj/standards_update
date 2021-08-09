import textract

text = textract.process('data.docx')

##str("text", "utf-8")

f = open("docdata.txt", "w")
##f.write(text)
f.close()