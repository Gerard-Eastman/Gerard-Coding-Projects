from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep


#folder to check
source_folder = "c:\\Users\\gerar\\Downloads"

#destination folders already exist
image_destination ="C:\\Users\\gerar\\OneDrive\\Desktop\\Images"
docs_destination = "C:\\Users\\gerar\\OneDrive\\Desktop\\Documents"
pdf_destination = "C:\\Users\\gerar\\OneDrive\\Desktop\\PDFs"
exe_destination = "C:\\Users\\gerar\\OneDrive\\Desktop\\executables"
video_destination = "C:\\Users\\gerar\\OneDrive\\Desktop\\Videos"

#associating file extensions with file types
image_ext = [".png", ".jpg", ".jpeg"]
docs_ext = [".docx", ".doc", ".ppt", ".pptx"]
exe_ext = [".exe"]
pdf_ext = [".pdf"]
video_ext = [".mp4"]


#file iterator calls subsequent functions
def file_iterator():
    with scandir(source_folder) as source_files:
        for current_file in source_files:
            file_name = current_file.name
            check_doc(current_file, file_name)
            check_exe(current_file, file_name)
            check_image(current_file, file_name)
            check_pdf(current_file, file_name)
            check_video(current_file, file_name)


#to make sure files not overwritten
def make_unique(destination, name_ext):
    name, ext = splitext(name_ext)
    counter = 1
    
    while exists(f"{destination}/{name_ext}"):
        name_ext = f"{name}({str(count)}){ext}"
        count += 1

    return name_ext

#moves files without overwriting
def move_file(destination, file_path, file_name):
    if exists(f"{destination}/{file_name}"):
        unique_name = make_unique(destination, file_name)
        oldName = join(destination, file_name)
        newName = join(destination, unique_name)
        rename(oldName, newName)
    move(file_path, destination)

#file checker functions check which extension it has, then sorts accordingly
def check_image(a_file, file_name):
    for ext in image_ext:
        if(file_name.endswith(ext)):
            move_file(image_destination, a_file, file_name)  
def check_doc(a_file, file_name):
    for ext in docs_ext:
         if(file_name.endswith(ext)):
            move_file(docs_destination, a_file, file_name)
def check_exe(a_file, file_name):
    for ext in exe_ext:
         if(file_name.endswith(ext)):
            move_file(exe_destination, a_file, file_name)
def check_pdf(a_file, file_name):
    for ext in pdf_ext:
         if(file_name.endswith(ext)):
            move_file(pdf_destination, a_file, file_name)
def check_video(a_file, file_name):
    for ext in video_ext:
         if(file_name.endswith(ext)):
            move_file(video_destination, a_file, file_name)




#running the functions to sort the files
file_iterator()



