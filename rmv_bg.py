# Remove Background of Images
# pip install rembg
# pip install pillow
from rembg import remove as rem
from PIL import Image
def Remove_bg(img):
    output = "removed_bg.png" 
    input = Image.open(img)
    output_img = rem(input)
    output_img.save(output)

image_name = input('Enter the full name of image: ') 
Remove_bg(image_name)