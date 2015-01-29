#!/usr/bin/env python

import json
import os
import argparse
from collections import OrderedDict
from string import Template

parser = argparse.ArgumentParser(description='Create new Python assignments.')
parser.add_argument('name', metavar="NAME", type=str,
                    help="URL-safe name for the assignment.")
parser.add_argument('-t', '--title', type=str,
                    help="The title of the assignment.")

args = parser.parse_args()

name = args.name
title = args.title or input("Title: ")
desc = input("Description: ")
keywords = []

print("Keywords (hit enter after each, hit it again when done):")

while True:
    keyword = input()
    if keyword == "":
        break
    else:
        keywords.append(keyword)

project_dict = OrderedDict([("name", name),
                            ("version", "0.0.1"),
                            ("title", title),
                            ("description", desc),
                            ("keywords", keywords)])

script_path = os.path.dirname(__file__)
project_path = os.path.join(script_path, "..", name)
template_path = os.path.join(script_path, "..", "template")

with open(os.path.join(template_path, "README.md"), "r") as file:
    readme_template = Template(file.read())

if not os.path.isdir(project_path):
    os.mkdir(project_path)

os.chdir(project_path)

with open(".homework.json", "w") as file:
    json.dump(project_dict, file, indent=2)

with open("README.md", "w") as file:
    file.write(readme_template.substitute(project_dict))
