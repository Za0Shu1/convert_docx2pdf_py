from docx2pdf import convert
import filedialogs
import time
import os

def del_file(folder):
    for file in os.listdir(folder):
        if(file.endswith(".docx")):
            os.remove(os.path.join(folder,file))
    pass

should_delete = input("delete file after convert? (y/n) \n") == 'y'

print("select pdf file folder...")
time.sleep(0.2)
FolderPath = filedialogs.open_folder_dialog('select pdf file folder', 'gbk')
if(FolderPath):
    print("you select {" + FolderPath + "} as the target pdf file folder \nconverting...")
else:
    print("user cancled.")
    time.sleep(1)
    quit(0)

convert(FolderPath)
if(should_delete):
    del_file(FolderPath)

print("task finished.")
time.sleep(1)
