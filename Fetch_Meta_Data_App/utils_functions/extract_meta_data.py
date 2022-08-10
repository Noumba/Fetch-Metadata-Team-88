# Import Libraries
import pikepdf
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from exif import Image
from PIL import Image as im

# Metadata
import exiftool

# Extract Pdf metadata


def get_pdf_metadata(filename):
    '''This function extract the metadata of pdf files and returns it as a dictionary object.'''
    pdf = pikepdf.Pdf.open(filename)
    docinfo = pdf.docinfo
    docinfo_dict = {}
    for key, value in docinfo.items():
        docinfo_dict[key] = str(value)
    return docinfo_dict


# Extract Media Metadata
def get_media_metadata(filename):
    '''This function returns the metadata of any supported file as a list

        params: filename - the name of the file passed
    '''
    file_parser = createParser(filename)
    if not file_parser:
        return "Unable to parse a file!!"
    with file_parser:
        try:
            file_metadata = extractMetadata(file_parser)
            return file_metadata.exportPlaintext()
        except Exception as err:
            file_metadata = None
            return file_metadata  # "Metadata Extraction Error!!"


test = get_media_metadata(
    'Fetch_Meta_Data_App/static/upload/image1.jpeg')


img_path = f'Fetch_Meta_Data_App/static/upload/80.png'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

# print(img.has_exif)


def get_metadata(filename):
    ''' This functions returns the metdata of any file as a dictionary'''
    try:
        with exiftool.ExifToolHelper() as et:
            metadata = et.get_metadata(filename)
        for meta_dict in metadata:
            return meta_dict
    except Exception as err:
        return None
