# Admin libraries
from importlib.metadata import metadata
from django.shortcuts import render
from django.http import HttpResponse, request
from django.core.files.storage import FileSystemStorage

from .forms import FileUpload

# Fetch metadata packages
from Fetch_Meta_Data_App.utils_functions.functions import handle_uploaded_file
from Fetch_Meta_Data_App.utils_functions.extract_meta_data import get_metadata

# Export filetype library
import json
# Create your views here.


def upload_file(request):
    '''Uploading File'''
    context = {}
    tags = []
    values = []
    file_path = ""
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['user_file'])
            uploaded_file = request.FILES['user_file']
            file_path = 'Fetch_Meta_Data_App/static/upload/'
            meta_data = get_metadata(file_path+str(uploaded_file))
            for key, value in meta_data.items():
                tags.append(key)
                values.append(value)
            context['metadata'] = zip(tags, values)
            context_dict = meta_data

            model_instance = form.save(commit=False)
            model_instance.save()

            request.session['metadata_session'] = context_dict

            return render(request, 'result.html', context)
    else:
        form = FileUpload()

    #meta_data_json = json.dumps(meta_data, indent=4)

    context['form'] = form
    return render(request, 'index.html', context)  # {'form': form})


def result_display():
    metadata = request.session.get("metadata_session")
    context = metadata
    return render(request, "index.html", context)


def save_metadata():
    pass


def download_metadata(request):
    metadata = request.session.get("metadata_session")
    json_writer = json.dumps(metadata, indent=4)
    response = HttpResponse(json_writer, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="metadata.json"'


def share_metadata():
    pass


def get_file():
    pass


def download_file():
    pass


def delete_file():
    pass
