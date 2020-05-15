# importing the needed libraries
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

# save the new csv
