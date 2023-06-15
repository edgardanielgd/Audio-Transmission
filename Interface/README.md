# To compile UserDialog.ui and all *.ui files

1) pip install pyside6-uic
2) run: `pyside6-uic <filename>.ui > <dest_filename>.py`
3) run: `pyside6-rcc Resources/<resourceName>.qrc -o <dest_filename>.py`
4) Now <dest_filename>.py has the class structure for the interface designed on PyDesigner

# Aditional libraries
-) 

