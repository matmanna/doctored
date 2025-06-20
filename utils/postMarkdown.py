# Adapted from a script by @JacobU on GitHub:
# https://github.com/JacobU/markdown-jekyll-preprocessor/blob/master/postMarkdown.py

# Notes:
### I modified it however so that footnotes, sidenotes and table of contents
### can be disabled in the frontmatter of the markdown file.
### Additionally, it now generates a "do not edit" comment at the top of the
### file to prevent accidental edits and uses the _drafts directory.

import sys, os, re

DO_NOT_EDIT_COMMENT = "\n<!-- This file is auto-generated based on a markdown file in _drafts. Do not edit directly. -->\n"

def getSmall(read_file, write_file, enable_sidenotes=True, enable_footnotes=True):
    if not enable_sidenotes:
        with open(read_file, "r") as rf, open(write_file, "w+") as wf:
            wf.write(rf.read())
        return
    with open(read_file, "r") as rf, open(write_file, "w+") as wf:
        lines = rf.readlines()
        count = 1
        for x in lines:
            startIndex = 0
            while startIndex < len(x):
                startIndex = x.find("<small>", startIndex)
                if startIndex == -1: break
                endIndex = x.find("</small>", startIndex)
                inside = x[startIndex + 7:endIndex]
                if enable_footnotes:
                    wf.write("[^" + str(count) + "]: " + inside + "\n")
                count += 1
                startIndex = endIndex + 8

def writeFootnote(read_file, write_file, enable_footnotes=True):
    if not enable_footnotes:
        with open(read_file, "r") as rf, open(write_file, "w+") as wf:
            wf.write(rf.read())
        return
    with open(read_file, "r") as rf, open(write_file, "w+") as wf:
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
        if (enable_footnotes):
            wf.write("\n\n\n## Footnotes \n")

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
        elif not content.startswith(DO_NOT_EDIT_COMMENT):
            f.seek(0)
            f.write(DO_NOT_EDIT_COMMENT + content)
            f.truncate()

def getHeaders(read_file, write_file):
    with open(read_file, "r") as rf:
        content = rf.read()
        frontmatter_match = re.search(r'---\s*(.*?)\s*---', content, re.DOTALL)
        frontmatter = frontmatter_match.group(1) if frontmatter_match else ""
        enable_footnotes = 'footnotes: false' not in frontmatter
        enable_sidenotes = 'sidenotes: false' not in frontmatter
        enable_toc = 'toc: false' not in frontmatter and frontmatter_match

    with open("temp1.txt", "w+") as ff:
        if not enable_toc:
            ff.write(content)
        else:           
            count, numLines = 0, 0
            with open(read_file, "r") as rf:
                lines = rf.readlines()
                for x in lines:
                    ff.write(x)
                    numLines += 1
                    if x.startswith("---"):
                        count += 1
                    if count == 2:
                        break
                
                for i, z in enumerate(lines):
                    if i >= numLines:
                        ff.write(z)

    print(read_file,enable_footnotes)
    writeFootnote("temp1.txt", "temp2.txt", enable_footnotes)
    getSmall("temp1.txt", "temp3.txt", enable_sidenotes, enable_footnotes)

    with open(write_file, "w+") as outfile:
        for file in ["temp2.txt", "temp3.txt"]:
            with open(file) as infile:
                outfile.write(infile.read())

    insert_do_not_edit_after_frontmatter(write_file)
    for temp_file in ["temp1.txt", "temp2.txt", "temp3.txt"]:
        os.remove(temp_file)

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
    else:
        read_file = sys.argv[1]
        output_filename = os.path.basename("_drafts/" + read_file)
        getHeaders("_drafts/" + read_file, output_filename)