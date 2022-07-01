"""
Usage: 

"""

import os
import argparse
from venv import create
import ast

total_contents = []
accepted_file_extensions = ['py']


parser = argparse.ArgumentParser(description='Provide directory for index build')
parser.add_argument("--path")
args = parser.parse_args()


def create_json(docstring):
    metadata = {}
    for line in docstring.split("\n"):
        key, value = line.split(":", 1)[0], line.split(":", 1)[1].strip()
        metadata[key] = value
    return metadata
        

if os.path.exists(os.path.join(".", args.path)):
    for root, dirs, files in os.walk(os.path.join(".", args.path)):
        for code_file in files:
            if code_file.split(".")[1] in accepted_file_extensions:
                with open(os.path.join(root ,code_file), 'r') as fp:
                    file_contents = fp.read()
                    module = ast.parse(file_contents)
                    docstring = ast.get_docstring(module)
                    metadata = create_json(docstring)
                    total_contents.append(metadata)
    print(total_contents)
else:
    raise Exception("No given directory")
