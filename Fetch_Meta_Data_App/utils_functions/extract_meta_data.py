# Import Libraries
import pikepdf


# Extract Pdf metadata
def get_pdf_metadata(filename):
    '''This function extract the metadata of pdf files and returns it as a dictionary object.'''
    pdf = pikepdf.Pdf.open(filename)
    docinfo = pdf.docinfo
    docinfo_dict = {}
    for key, value in docinfo.items():
        docinfo_dict[key] = str(value)
    return docinfo_dict
