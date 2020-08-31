#!/usr/bin/python
############################################################
#
# Zip Latex V3
#
# Packs all your TeX files in an archive for submission of
# camera-ready versions in an easily customizable manner.
#
# AUTHOR:
#   *  Richard Lindner <rlindner@cdc.informatik.tu-darmstadt.de>
#
############################################################
from os import curdir, walk
from os.path import basename, abspath, join, isfile, splitext
from zipfile import ZipFile, ZIP_DEFLATED

texfiles = list()
arc_name = basename(abspath(curdir)) + '.zip'
for root, dirs, files in walk(curdir):
    for file in files:
        if file == 'ziplatex.py': continue
        fullpath = join(root, file)
        file_ext = splitext(file)[-1].lower()
        keep_ext = list()

        # TeX
        keep_ext += ['.tex', '.bib', '.bst', '.cls', '.sty']
        # TeX-Figures
        keep_ext += ['.plt', '.pstex', '.pstex_t', '.jpg', '.png', '.eps']
        # Scripts: Python, SAGE, Pari
        keep_ext += ['.bat', '.py', '.sage', '.gp']
        # TeXniccenter, Dia
        keep_ext += ['.tpc', '.dia']
        # Documents Adobe, Microsoft, Open/Libreoffice
        keep_ext += ['.ps', '.pdf']
        keep_ext += ['.doc', '.docx', '.xls', '.xlsx',  '.ppt',  '.pptx']
        keep_ext += ['.odt', '.ods', '.odp']
       
        if file_ext in keep_ext:
            texfiles.append(fullpath)

fout_arc = ZipFile(arc_name, 'w', compression=ZIP_DEFLATED)
print 'creating', arc_name, 'with'
for file in texfiles:
    print file
    fout_arc.write(file)
fout_arc.close()
