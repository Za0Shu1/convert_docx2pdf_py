import xlrd
import xlwt
import os

# write
workbook = xlwt.Workbook(encoding='utf8')
worksheet = workbook.add_sheet(u'Sheet1')

# just for example
folder = 'C:\\Users\\DIY\\Desktop\\pdfs'
row = 0
files = os.listdir(folder)

# filename templates : 1-xxx;2-xxx;...;10-xxx...
temp_files = []
for temp_file in files:
    if(temp_file.endswith('.pdf')):
        if(temp_file[1] == '-'):
            temp_file = '0' + temp_file
        temp_files.append(temp_file)

# sort by filename index
temp_files.sort(key=lambda x:int(x[:2]))
for file in temp_files:
    if (file.endswith(".pdf")):
        file = file.lstrip('0')
        worksheet.write(row,0,label=file)
        print(file)
        row += 1

workbook.save('pdf_filenames.xls')

