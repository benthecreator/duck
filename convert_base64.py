import base64

# Path to your image file
image_path = "hugeDuck.png"

# Read the image file and encode it to base64
with open(image_path, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Write the base64 string to image_data.txt
with open('image_data.txt', 'w') as output_file:
    output_file.write(encoded_string)