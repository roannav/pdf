# print the text from a pdf file.  optionally specify which pages.
#
# Usage:
# py get_text_from_pdf filename.pdf [start_page] [end_page]
#
# start_page and end_page are indexed with the first page being page 1.
# end_page (optional): This is the last page to scan
# start_page (optional): This is the first page to scan.
#    If no end_page argument is given, then start_page is the only page to scan
#
# Example:  get_text_from_pdf newsletter.pdf 3
#    ==> will return the text from the 3rd page only.

import PyPDF2
import sys

# This script uses 1-based index, however
# PyPDF2 uses 0-based index.
num_args = len(sys.argv)
if num_args >= 4:
    end_page = sys.argv[3] - 1

start_page = 0
if num_args >= 3:
    start_page = sys.argv[2] - 1

if num_args >= 2:
    filename = sys.argv[1]
else:
    print("ERROR: please supply a pdf filename")
    print("Usage:")
    print("py get_text_from_pdf filename.pdf [start_page] [end_page]")
    sys.exit()

pdf_file = open(filename, "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print(pdf_reader.numPages)

for i in range(1):
    page = pdf_reader.getPage(i)
    print(page.extractText())

