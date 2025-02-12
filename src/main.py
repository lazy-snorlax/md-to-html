from textnode import TextNode
import pathlib
import shutil
import os

project_directory = pathlib.Path().resolve()
dir_path_static = "./static"
dir_path_public = "./public"

def copy_files_recursive(source_dir_path, dest_file_path):
    if not os.path.exists(dest_file_path):
        os.mkdir(dest_file_path)
    
    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_file_path, filename)
        print(f" * {from_path} -> {dest_path}")

        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def main():
    print('Deleting public directory... ')
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copy static files to public directory")
    copy_files_recursive( dir_path_static, dir_path_public)

main()

