from exif import Image
f = "./back.jpg"
with open(f, 'rb') as image_file:
    my_image = Image(image_file)
print(my_image.has_exif)
print(my_image.list_all())
print(my_image.gps_img_direction)
