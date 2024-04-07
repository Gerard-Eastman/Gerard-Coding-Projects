from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging

#folder to check
source_folder = "c:\Users\gerar\Downloads"
#destination folders
image_destination ="C:\Users\gerar\OneDrive\Desktop\Images"
docs_destination = "C:\Users\gerar\OneDrive\Desktop\Documents"
pdf_destination = "C:\Users\gerar\OneDrive\Desktop\PDFs"
exe_destination = "C:\Users\gerar\OneDrive\Desktop\executables"
video_destination = "C:\Users\gerar\OneDrive\Desktop\Videos"

#associating file extensions with file types
image_ext = [".png", ".jpg", ".jpeg"]
docs_ext = [".docx", ".doc", ".ppt", ".pptx"]
exe_ext = [".exe"]
pdf_ext = [".pdf"]
video_ext = [".mp4"]

#file finder calls checker functions
def file_iterator():
    with scandir(source_folder) as file_names:
        for file_name in file_names:


#file checker functions check
def check_image(entry, name):
    for x in image_ext

def check_doc():
    pass

def check_exe():
    pass
def check_pdf():
    pass
def check_video():
    pass