# Adapted from a script by @JacobU on GitHub:
# https://github.com/JacobU/markdown-jekyll-preprocessor/blob/master/postMarkdown.py

import sys
import os
import re

DO_NOT_EDIT_COMMENT = "\n<!-- This file is auto-generated based on a markdown file in _drafts. Do not edit directly. -->\n"

def getSmall(read_file, write_file):
    
    with open(read_file, "r") as rf:
        with open(write_file, "w+") as wf:
                if rf.mode == "r":
                    lines = rf.readlines()
                    count = 1

                    for x in lines:
                        startIndex = 0
                        endIndex = 0
                        while startIndex < len(x):
                            startIndex = x.find("<small>", startIndex)
                            if startIndex == -1:
                                break
                            endIndex = x.find("</small>", startIndex)
                            inside = x[startIndex + 7:endIndex]
                            wf.write("[^" + str(count) + "]: " + inside + "\n")
                            count += 1
                            startIndex = endIndex + 8
                        
    rf.close()
    wf.close()

def writeFootnote(read_file, write_file):

    with open(read_file, "r") as rf:
        with open(write_file, "w+") as wf:
                if rf.mode == "r":
                    lines = rf.readlines()
                    count = 1

                    for x in lines:
                        index = 0
                        while index < len(x):
                            temp = index
                            index = x.find("</small>", index)
                            if index == -1:
                                wf.write(x[temp:])
                                break                        

                            index += 8
                            wf.write(x[temp:index] + "[^" + str(count) + "]")
                            count += 1
                wf.write("\n\n")
    rf.close()
    wf.close()

def prepend_do_not_edit_comment(filepath):
    with open(filepath, "r+") as f:
        content = f.read()
        if not content.startswith(DO_NOT_EDIT_COMMENT):
            f.seek(0)
            f.write(DO_NOT_EDIT_COMMENT + content)
            f.truncate()

def insert_do_not_edit_after_frontmatter(filepath):
    with open(filepath, "r+") as f:
        content = f.read()
        frontmatter_ends = [m.start() for m in re.finditer(r'^---\s*$', content, re.MULTILINE)]
        if len(frontmatter_ends) >= 2:
            insert_pos = frontmatter_ends[1] + len('---\n')
            after_frontmatter = content[insert_pos:insert_pos+len(DO_NOT_EDIT_COMMENT)]
            if after_frontmatter != DO_NOT_EDIT_COMMENT:
                new_content = content[:insert_pos] + DO_NOT_EDIT_COMMENT + content[insert_pos:]
                f.seek(0)
                f.write(new_content)
                f.truncate()
        else:
            if not content.startswith(DO_NOT_EDIT_COMMENT):
                f.seek(0)
                f.write(DO_NOT_EDIT_COMMENT + content)
                f.truncate()

def getHeaders(read_file, write_file):

    with open(read_file, "r") as rf:
        content = rf.read()
        frontmatter_match = re.search(r'---\s*(.*?)\s*---', content, re.DOTALL)
        
        if frontmatter_match and 'toc: false' in frontmatter_match.group(1):

            with open("temp1.txt", "w+") as ff:
                ff.write(content)
            
            with open("temp.txt", "w+") as wf:
                pass
        else:
            with open(read_file, "r") as rf:
                with open("temp.txt", "w+") as wf:
                    if rf.mode == "r":
                        lines = rf.readlines()

                        wf.write("\n")
                        for x in lines:
                            if(x[0:3] == "## "):
                                wf.write("- " + x[3:])
                            if(x[0:4] == "### "):
                                wf.write("\t- " + x[4:])
                            if(x[0:5] == "#### "):
                                wf.write("\t\t- " + x[5:])
                            if(x[0:6] == "##### "):
                                wf.write("\t\t\t- " + x[6:])
                        wf.write("\n")
            
            with open(read_file, "r") as rf:
                with open("temp.txt", "r") as wf:
                    with open("temp1.txt","w+") as ff:
                        if rf.mode == "r" and wf.mode == "r":
                            linesMain = rf.readlines()
                            linesHeaders = wf.readlines()
                            count = 0
                            numLines = 0

                            for x in linesMain:
                                ff.write(x)
                                numLines += 1
                                if(x[0:3] == "---"):
                                    count += 1
                                if(count == 2):
                                    break
                            
                            for y in linesHeaders:
                                ff.write(y)

                            count = -1
                            for z in linesMain:
                                count += 1
                                if(count > numLines):
                                    ff.write(z)

    os.remove("temp.txt")
    writeFootnote("temp1.txt", "temp2.txt")
    getSmall("temp1.txt", "temp3.txt")

    filenames = ["temp2.txt", "temp3.txt"]
    with open(write_file, "w+") as outfile:
        for file in filenames:
            with open(file) as infile:
                outfile.write(infile.read())

    insert_do_not_edit_after_frontmatter(write_file)

    os.remove("temp1.txt")
    os.remove("temp2.txt")
    os.remove("temp3.txt")

if __name__ == "__main__":

    if len(sys.argv) != 2:
        drafts_dir = "_drafts"
        if not os.path.isdir(drafts_dir):
            sys.exit(1)
        
        for root, dirs, files in os.walk(drafts_dir):
            for filename in files:
                file_path = os.path.join(root, filename)
            
                rel_path = os.path.relpath(file_path, drafts_dir)
                output_dir = os.path.dirname(rel_path)
            
                if output_dir and output_dir != '.':
                    os.makedirs(output_dir, exist_ok=True)
                    output_filename = os.path.join(output_dir, os.path.basename(file_path))
                else:
                    output_filename = os.path.basename(file_path)
                
                getHeaders(file_path, output_filename)
        sys.exit(0)
    else:
        read_file = sys.argv[1]
        output_filename = os.path.basename(read_file)
        getHeaders(read_file, output_filename)
