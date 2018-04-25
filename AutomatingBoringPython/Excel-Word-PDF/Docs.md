# [Excel, Docs, and PDF](https://automatetheboringstuff.com/chapter12/)

## Opening and reading Excel

* `openpyxl` module allow python program to read/modify Excel spreadsheet.

* `workbook = openpyxl.load_workbook('workbook.xlsx')` open workbook and return workbook object

* `sheet = workbook.get_sheet_by_name('Sheet1')` if you know what sheet you want to work with

* `workbook.get_sheet_names()` will return a list of available sheets

* `cell = sheet['CellLocation'].value` will return a cell object for us to work with that cell and the value for that cell

* `sheet.cell(row=row, column=column)` to specify what row and column you want


## Editing Excel (See Example Codes)

* `wb = openpyxl.Workbook()` to create a new Excel spreadsheet

* `wb.save()` to save the Workbook

* `sheet1 = wb.create_sheet()` to create new sheet


## Reading/Editing PDF

* They are binary files which are more complicated than text files.

* PDF layouts are not clear enough for software to fully read and parse them so it might be buggy to extract them 100%

* Install the 3rd party module PyPDF2 and `import PyPDF2` to work with PDF

* PDF2 cannot extract images or media but can extract full text

* You cannot write PDF from scratch but you can use other pdf and edit them into a new pdf

* See Sample Codes

## Word Docs

* Install the 3rd party module `python-docx` -> `import docx`

*
