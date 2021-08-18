import docx2txt
import re

document = docx2txt.process('C:/Users/nicobrits/PycharmProjects/standards_update/data.docx')

f = open('docdata.txt', 'w')
f.write(document)
f.close()

f = open('docdata.txt', 'r')
document = f.read()
f.close()


std_list_raw = re.findall(r'[E][N]\s\d{3,5}\s\-\s\w.+[^.]', document)
en_description_final =  []
for item in std_list_raw:
    en_description_final.append(item.strip())
print(en_description_final)

std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}\s\-\s\w.+[^.]', document)
iec_description_final = []
for item in std_list_raw:
    iec_description_final.append(item.strip())
print(iec_description_final)

std_list_raw = re.findall(r'[E][N]\s\d{3,5}', document)
en_list_final =  []
for item in std_list_raw:
    en_list_final.append(item.strip())
print(en_list_final)

std_list_raw = re.findall(r'[I][E][C]\s\d{3,5}', document)
iec_list_final = []
for item in std_list_raw:
    iec_list_final.append(item.strip())
print(iec_list_final)