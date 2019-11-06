import xlrd
import consts

# Takes in the name of a file and returns a list of the names in column A
# without class names and a dictionary where a person's name is the key and
# their email is the value
def sheet_to_list():
    # Set up Excel sheet
    loc = "./"
    path = loc + consts.file_name # Path to the file
    wb = xlrd.open_workbook(path) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0)

    names = [] # Holds the returned value
    emails = {} # Holds returned value

    for i in range(1, sheet.nrows): # Skips the label row
        if(sheet.cell_value(i, consts.col_emails) != ""): # Checks for class names
            names.append(sheet.cell_value(i, consts.col_names))
            emails[sheet.cell_value(i, consts.col_names)] = sheet.cell_value(i, consts.col_emails)
    
    #print(names) # Testing
    return names, emails
