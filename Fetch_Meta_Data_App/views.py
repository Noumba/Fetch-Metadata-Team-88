# Admin libraries
from django.shortcuts import render
from django.http import HttpResponse
from Fetch_Meta_Data_App.utils_functions.functions import handle_uploaded_file
from Fetch_Meta_Data_App.utils_functions.extract_meta_data import get_metadata
from .forms import FileUpload

# Fetch metadata packages


# Create your views here.
def upload_file(request):
    '''Uploading File'''
    meta_data = ""
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['user_file'])
            meta_data = get_metadata(request.FILES['user_file'])
            # print(meta_data)
            # return HttpResponse('File Uploaded Succesfully!')
            return HttpResponse(meta_data)
    else:
        form = FileUpload()
    context = {"metadata": meta_data, 'form': form}

    return render(request, 'index.html', context)  # {'form': form})


def save_metadata():
    pass


def download_metadata():
    pass


def share_metadata():
    pass
