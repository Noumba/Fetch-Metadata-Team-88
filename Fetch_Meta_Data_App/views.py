# Admin libraries
from django.shortcuts import render
from django.http import HttpResponse, request
from Fetch_Meta_Data_App.utils_functions.functions import handle_uploaded_file
from Fetch_Meta_Data_App.utils_functions.extract_meta_data import get_metadata
from .forms import FileUpload

import json

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
            file_type = meta_data.content_type.split("/")
            # print(meta_data)
            # return HttpResponse('File Uploaded Succesfully!')

            # return HttpResponse({"meta_data": meta_data})
    else:
        form = FileUpload()

    meta_data_json = json.dumps(meta_data, indent=4)

    context = {"metadata": meta_data_json, 'form': form}
    request.session['metadata'] = context
    return render(request, 'index.html', context)  # {'form': form})


def result_display():
    metadata = request.session.get("metadata")
    context = metadata
    return render(request, "index.html", context)


def save_metadata():
    pass


def download_metadata():
    pass


def share_metadata():
    pass


def get_file():
    pass


def download_file():
    pass


def delete_file():
    pass
