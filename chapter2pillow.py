from PIL import Image
from PIL import ImageFilter
from PIL import ImageFilter, Image

# Memuat gambar
Image = Image.open('bucket1.jpg')

Image.save('bucket1.jpg')


cropped_Image = Image.crop((10, 10, 200, 200))
cropped_Image.save('bucket1.jpg')

resized_Image = cropped_Image.resize((100, 100))
resized_Image.save('bucket1.jpg')

filtered_Image = resized_Image.filter(ImageFilter.BLUR)
filtered_Image.save('bucket1.jpg')

if filtered_Image.mode == 'RGBA':
    filtered_Image = filtered_Image.convert('RGB')