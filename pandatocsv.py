import base64, csv, os, pandas as pd

entries = os.listdir('/home/omer/Desktop/images/images')
file = open('/home/omer/Desktop/images/table.csv')

data = pd.read_csv(file)

code = []
image = []

for entry in entries:
    mod_entry = os.path.splitext(entry)[0]
    code.append(mod_entry)
    # converting images to binary and save it into the correspondent column
    with open(("/home/omer/Desktop/images/images/"+entry), "rb") as image_file:
        a = base64.b64encode(image_file.read())
        image.append(a)

data["code"] = code
data["image"] = image

data.to_csv("test.csv")