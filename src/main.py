import shutil
import os
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

# project_directory = Path().resolve()
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    basepath = sys.argv[1]
    if basepath is None:
        basepath = '/'
    print(f'Deleting {dir_path_public} directory... ')
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    else:
        os.mkdir(dir_path_public)
    
    print("Copy static files to public directory")
    copy_files_recursive( dir_path_static, dir_path_public)

    generate_pages_recursive("./content", "template.html", f"{dir_path_public}", basepath)

main()

