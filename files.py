import os
def rename_files():
    #get file names from the folder
    file_list=os.listdir(r"C:\Python27\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("current working directory is"+saved_path)
    os.chdir(r"C:\Python27\prank")
   
    #for each file,rename filename
    for file_name in file_list:
        print("old name" +file_name)
        print("new name" +file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
