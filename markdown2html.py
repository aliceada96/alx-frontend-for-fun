#!/usr/bin/python3
"""This script converts Markdown to HTML"""

import os
import re
import sys


def markdown_to_html(markdown_file, output_file):
    """Converts a given Markdown file into an HTML and
    writes the output into a new file"""

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py markdown_file output_file",
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print(f"Error: Missing file {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    # read markdown file and convert to html
    with open(markdown_file, 'r') as f:

        html = ""
        line = ""
        level = 1

        for char in f:
            if char == "\n":
                if line.startswith("#") and level <= 6:
                    html += f"<h{level}>{line[1:]}</h{level}>\n"
                elif line.strip():
                    html += f"<p>{line}</p>\n"
                line = ""
                level = 1
            elif char == "#":
                line += char
                level += 1
            else:
                line += char

    with open(output_file, 'w', encoding="utf-8") as f:
        f.write(html)


print("")
sys.exit(0)
