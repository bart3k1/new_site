import PIL
from PIL import Image
from PIL import ExifTags

# exifData = {}
# img = Image.open("/home/satq/Documents/Pythony/new_site/foto/foto.jpg")
# exifDataRaw = img._getexif()
# for tag, value in exifDataRaw.items():
#     decodedTag = ExifTags.TAGS.get(tag, tag)
#     exifData[decodedTag] = value





img = PIL.Image.open("/home/satq/Documents/Pythony/new_site/foto/foto.jpg")

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
