import PIL
from PIL import Image
from PIL import ExifTags

img = PIL.Image.open("/home/satq/Documents/Pythony/new_site/foto/foto.jpg")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
