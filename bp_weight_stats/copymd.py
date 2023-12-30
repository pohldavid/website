#!/usr/bin/python3

""" copy the files to the target directory """
# DGP 2023-12-21

import shutil



destination_path = '/home/dave/Desktop/website/static/weight-bp/'

files = ['bp.md', 'weight.md']

for file in files:
    source = file
    destination = destination_path + file
    shutil.copy2(source, destination)
    
