#This script was written by SigmaRelief
#Version 1.0.0 2020-06-22
#https://github.com/SigmaRelief/SOLIDWORKS-Export-to-Mesh

# importing required modules 
from zipfile import ZipFile
import io
import os
import tempfile
import sys 

def updateZip(zipname, filename, data):
    # generate a temp file
    tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
    os.close(tmpfd)

    # create a temp copy of the archive without filename            
    with ZipFile(zipname, 'r') as zin:
        with ZipFile(tmpname, 'w') as zout:
            zout.comment = zin.comment # preserve the comment
            for item in zin.infolist():
                if item.filename != filename:
                    zout.writestr(item, zin.read(item.filename))

    # replace with the temp archive
    os.remove(zipname)
    os.rename(tmpname, zipname)

    # now add filename with its new data
    with ZipFile(zipname, 'a') as zf:
        zf.writestr(filename, data)


#variables
file_path = sys.argv[1]
file_name = os.path.basename(file_path)
inner_file_path = "3D/"
inner_file_name = "3dmodel.model"

with ZipFile(file_path, 'r') as archive:

    with io.TextIOWrapper(archive.open(inner_file_path + inner_file_name), encoding="utf-8") as f:
        f_content = f.readlines()

        #calculated variables
        sizeoflist = len(f_content)

        body_count = 0
        body_id = 1
        file_name_noex = file_name[:-4]

        #count number of bodies in file
        for i in range(sizeoflist):
            line = f_content[i]
            body_count = body_count + line.count(""" name="body""")

        #loop through entire file to replace name
        for i in range(sizeoflist):
            match_start = 0
            line = f_content[i]

            #check for matches
            while match_start >= 0:
                match_start = line.find(""" name="body""")
                match_end = line.find("""" """, match_start + 8)

                #if multiple bodies edit line
                if match_start > 0 and body_count > 1:
                    line = line[0:match_start + 7] + file_name_noex + "-" + str(body_id) + line[match_end:]
                    body_id += 1

                #if single body edit line
                if match_start > 0 and body_count == 1:
                    line = line[0:match_start + 7] + file_name_noex + line[match_end:]

            #store edited line
            f_content[i] = line

format_content = ("".join(f_content))
format_content = format_content.replace("\n", "\r\n")

updateZip(file_path, inner_file_path + inner_file_name, format_content)