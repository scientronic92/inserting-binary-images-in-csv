import base64, csv, os, numpy as np

file = open('/home/omer/Desktop/images/table.csv')
csv_file = csv.reader(file)
# csv_array = np.genfromtxt(file, delimiter=";", skip_header=1)

entries = os.listdir('/home/omer/Desktop/images/images')

# loop into images and insert it to the correspondent name in the csv file
for entry in entries:
    mod_entry = os.path.splitext(entry)[0]
    for i in csv_file:
        csv_file[i][0] = mod_entry
        # converting images to binary and save it into the correspondent column
        csv_file[i][1] = base64.b64encode(entry.read())
