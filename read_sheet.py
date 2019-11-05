import xlrd
import consts

# Takes in the name of a file and returns a list of the names in column A
# without class names.
def sheet_to_list():
    # Set up Excel sheet
    loc = "./"
    path = loc + consts.file_name # Path to the file
    wb = xlrd.open_workbook(path) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0)

    names = [] # Holds the returned value

    for i in range(1, sheet.nrows): # Skips the label row
        if(sheet.cell_value(i, consts.col_emails) != ""): # Checks for class names
            names.append(sheet.cell_value(i, consts.col_names))
    
    #print(names) # Testing
    return names

# Takes in the name of a file and returns a dictionary where each key is a
# person's full name from column A and its value is their email address from
# column D.
def email_dict():
    # Set up Excel sheet
    loc = "./"
    path = loc + consts.file_name # Path to the file
    wb = xlrd.open_workbook(path) 
    sheet = wb.sheet_by_index(0) 
    sheet.cell_value(0, 0)

    emails = {} # Holds returned value

    for i in range(1, sheet.nrows): # Skips the label row
        if(sheet.cell_value(i, consts.col_emails) != ""): # Checks for class names
            emails[sheet.cell_value(i, consts.col_names)] = sheet.cell_value(i, consts.col_emails)

    #print(emails) # Testing
    return emails
