# Prints the text from a pdf file.  Optionally specify which pages.
#
# Usage:
# py get_text_from_pdf filename.pdf [start_page] [end_page]
#
# start_page and end_page are indexed with the first page being page 1.
# start_page (optional): This is the first page to scan.
# end_page (optional): This is the last page to scan.
# If no end_page argument is given, then start_page is the only page to scan.
#
# Example:  get_text_from_pdf newsletter.pdf 3
#    ==> returns the text from the 3rd page only.

import PyPDF2
import sys

num_args = len(sys.argv)

if num_args >= 2:
    filename = sys.argv[1]
else:
    print("ERROR: please supply a pdf filename")
    print("Usage:")
    print("py get_text_from_pdf filename.pdf [start_page] [end_page]")
    sys.exit()


# This script uses 1-based index, however
# PyPDF2 uses 0-based index.
start_page = 0
if num_args >= 3:
    start_page = int(sys.argv[2]) - 1
    assert start_page >= 0, "start_page should be a positive integer"

if num_args >= 4:
    end_page = int(sys.argv[3]) - 1
    assert end_page >= start_page, "end_page should be same or after start_page"
else:
    end_page = start_page


pdf_file = open(filename, "rb")
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
print(pdf_reader.numPages)
assert start_page < pdf_reader.numPages, "start_page is too large"
assert end_page < pdf_reader.numPages, "end_page is too large"

for i in range(start_page, end_page + 1):
    page = pdf_reader.getPage(i)
    print(f"The text from page #{i+1}")
    print(page.extractText())

