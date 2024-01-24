#!/usr/bin/python3
"""This script converts Markdown to HTML"""

import os
#import re
import sys

#def markdown_to_html(markdown_file, output_file):
#   """Converts a given Markdown file into an HTML and 
#        writes the output into a new file"""
    

if len(sys.argv) != 3:
    print("Usage: ./markdown2html.py markdown_file output_file", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Error: Missing file {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)

# Conversion code here

print("")
sys.exit(0)
