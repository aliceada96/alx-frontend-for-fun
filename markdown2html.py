#!/usr/bin/python3
"""This script converts Markdown to HTML"""

import os
import re
import sys


def markdown_to_html(markdown_file, output_file):
    """Converts a given Markdown file into an HTML and
    writes the output into a new file"""

    if not os.path.isfile(sys.argv[1]):
        print(f"Error: Missing file {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    # read markdown file and convert to html
    with open(markdown_file, 'r') as f:

        final_html = []

        for line in f:
            match = re.match(r"^(#+) (.*)$", line)
            if match:
                heading_level = len(match.group(1))
                heading_text = match.group(2)
                final_html.append(
                    f"<h{heading_level}>{heading_text}</h{heading_level}>")
            else:
                final_html.append(line.rstrip())

        for line in f:
            match_ul = re.match(r"^- (.*)$", line)
            if match_ul:
                list_text = [match_ul.group(1)]
                final_html.append(f"<ul><li>{list_text[0]}</li></ul>")
            else:
                final_html.append(line.rstrip())

    with open(output_file, 'w', encoding="utf-8") as f:
        f.write("\n".join(final_html))

if __name__ == "__main__":


    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py markdown_file output_file",
              file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    markdown_to_html(markdown_file, output_file)

    sys.exit(0)
