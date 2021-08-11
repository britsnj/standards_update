import docx2txt
import re

document = docx2txt.process('C:/Users/brits/Standards Updater/standards_update/data.docx')

f = open('docdata.txt', 'w')
f.write(document)
f.close()

f = open('docdata.txt', 'r')
document = f.read()
f.close()


std_list_raw = re.findall(r'[E]+[N]+\s+[\d{5}]\w.+[^.]', document)

std_list_en_final =  []

for item in std_list_raw:
    std_list_en_final.append(item.strip())

print(std_list_en_final)