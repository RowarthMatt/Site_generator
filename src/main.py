import os
import shutil

from textnode import *
from htmlnode import *
from inline_markdown import *
from markdown_blocks import *

def copy_file(source):
    if os.path.exists(source):
        if not os.path.exists("public") and source == "static":
            os.mkdir("public")
        elif source == "static":
            shutil.rmtree("public")
            os.mkdir("public")
        

        contents = os.listdir(source)
        print(contents)
        for file in contents:
            path = os.path.join(source, file)
            new_path = path.replace("static", "public")
            if os.path.isfile(path):
                shutil.copy(path, new_path)
                print(f"file found: {path}")
            else:
                print(f"Directory found: {path}")
                os.mkdir(new_path)
                copy_file(path)
    else:
        print("Directory doesn't exist")

def main():
    copy_file("static")
    
main()
