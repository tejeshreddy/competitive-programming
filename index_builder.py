"""
Usage: 

"""

import os
import argparse

accepted_file_extensions = ['py']

parser = argparse.ArgumentParser(description='Provide directory for index build')
parser.add_argument("--directory")
args = parser.parse_args()

if os.path.exists(os.path.join(".", args.directory)):
    for root, dirs, files in os.walk(os.path.join(".", args.directory)):
        for code_file in files:
            if code_file.split(".")[1] in accepted_file_extensions:
                with open(os.path.join(root ,code_file), 'r') as fp:
                    file_contents = fp.read()
                print(file_contents)                 
else:
    raise Exception("No given directory")
