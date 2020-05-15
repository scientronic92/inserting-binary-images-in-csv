# importing the needed libraries
import base64, csv, os

file = open('file.csv')
csv_file = csv.reader(file)

# reading the directory list of files
entries = os.listdir('/home/omer/Desktop/images/')

# loop into images and insert it to the correspondent name in the csv file
for entry in entries:
    for i in csv_file:
        if csv_file[i][0] == entry:
            # converting images to binary and save it into the correspondent column
            csv_file[i][5] = base64.b64encode(entry.read())

# save the new csv
