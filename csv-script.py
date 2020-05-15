# importing the needed libraries
<<<<<<< HEAD
import base64, csv_creator, os, numpy as np

file = open('/home/omer/Desktop/images/1.csv')
csv_array = np.genfromtxt(file, delimiter=";", skip_header=1)
    #csv.reader(file)

# reading the directory list of files
entries = os.listdir('/home/omer/Desktop/images/images')

# loop into images and insert it to the correspondent name in the csv file
for entry in entries:
    mod_entry = os.path.splitext(entry)[0]
    for i in csv_array:
        if csv_array[i][0] == mod_entry:
            # converting images to binary and save it into the correspondent column
            csv_array[i][5] = base64.b64encode(entry.read())
=======
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
>>>>>>> 09267c54b2bbc699394a4d0a7abd0e6ffb758ba0

# save the new csv
workbook = xlrd.open_workbook("table.xlsx")
sheet = workbook.sheet_by_index(0)

for rowx in range(sheet.nrows):
    values = sheet.row_values(rowx)
    print(values)