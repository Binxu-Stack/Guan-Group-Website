#!/usr/bin/env python

import re

def insert_content2base(content, output, base="base.html"):
    print("Converting "+ content + " ...")

    # read all content
    with open(content,"r") as indata:
        xx = indata.read()
    

    # open output
    out = open(output,"w")

    # begin string and end string
    bs = r"<!-- content begin -->"
    es = r"<!-- content end -->"
    stop = 0
    with open(base,"r") as indata:
        for line in indata:
            if re.search(bs, line):
                out.write(xx)
                # change state to stop write lines
                stop = 1
            elif re.search(es,line):
                # change state to write lines
                stop = 0
            if stop == 0:
                out.write(line)
    print("Converting finished. Output: " + output)
    print()

insert_content2base("./index_content.html","index.html")
insert_content2base("./people_content.html","people.html")
insert_content2base("./contact_content.html","contact.html")
insert_content2base("./opening_content.html","opening.html")
insert_content2base("./teaching_content.html","teaching.html")
insert_content2base("./research_content.html","research.html")
import os
print("Creating publications.html...")
os.system("./All_publications/bibtex2html.py ./All_publications/Guan_new.bib base.html publications.html")
print("Creating publications.html finished.")

print("Copying files to ../2-view")
cmd = """
[ -d ../2-view ] || mkdir ../2-view
cp index.html people.html contact.html publications.html ./opening.html ./research.html ./teaching.html   ../2-view
cp -r semantic.min.css  w3.css my.css img semantic.min.js ../2-view
"""
os.system(cmd)
print("Done")
