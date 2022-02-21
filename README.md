# get_text_from_PDF.py

Prints the text from a pdf file.  Optionally specify which pages.

Usage:
py get_text_from_pdf filename.pdf [start_page] [end_page]

start_page and end_page are indexed with the first page being page 1.
start_page (optional): This is the first page to scan.
end_page (optional): This is the last page to scan.
If no end_page argument is given, then start_page is the only page to scan.

Example:  get_text_from_pdf newsletter.pdf 3
   ==> returns the text from the 3rd page only.
