# importing the needed libraries
import base64, csv, os, xlrd

# file = open('table.xlsx')
# csv_file = csv.reader(file)

# # reading the directory list of files
# entries = os.listdir('./images/')

# # loop into images and insert it to the correspondent name in the csv file
# for entry in entries:
#     for i in csv_file:
#         if csv_file[i][4] == entry:
#             # converting images to binary and save it into the correspondent column
#             csv_file[i][5] = base64.b64encode(entry.read())

# save the new csv
workbook = xlrd.open_workbook("table.xlsx")
sheet = workbook.sheet_by_index(0)

for rowx in range(sheet.nrows):
    values = sheet.row_values(rowx)
    print(values)