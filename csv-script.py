# importing the needed libraries
import base64, csv, os

# a function reading images in base64 format
def encode_image(path):
    with open("./images/{}".format(path), "rb") as img:
        return base64.b64encode(img.read())

#opening the old CSV
with open('table.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    #creating a new CSV
    with open('new_table.csv', 'w') as new_file:

        #creating the header for the new CSV
        fieldnames = ['name',"Country of Origin","Unit of Quantity",
            "Product description", "product_code", "images(base64)"]

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader() #writing the head of the CSV file

        images = os.listdir('./images')

        for old_line in csv_reader:

            new_img = {"images(base64)" : ""}
            new_line = dict(old_line, **new_img)

            for img in images:
                # checking if the product code is equal to the image name
                # without the '.png' format characters
                if old_line['product_code'] == img[:-4]: 
                    new_img = {"images(base64)" : encode_image(img)}
                    # for combining two dictionaries into one
                    new_line = dict(old_line, **new_img)
                    break

            csv_writer.writerow(new_line)
