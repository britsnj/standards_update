import docx2txt
import re

document = docx2txt.process('C:/Users/brits/Standards Updater/standards_update/data.docx')

f = open('docdata.txt', 'w')
f.write(document)
f.close()

f = open('docdata.txt', 'r')
document = f.read()
f.close()


std_list = re.findall(r'[E]+[N]+\s+\d{5}', document)

print(std_list)