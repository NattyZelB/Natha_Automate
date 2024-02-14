from django.contrib import messages
from django.shortcuts import render, redirect

from awd_main import settings
from dataentry.utils import get_all_custom_models
from uploads.models import Upload
from django.core.management import call_command

def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')

        #dtore this file inside the upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        #construct the full path
        realative_path = str(upload.file.url)
        # call setting BASE_DIR ROOT from settings
        base_url = str(settings.BASE_DIR)

        file_path = base_url+realative_path
        print(file_path)
        #trigger the import data commad
        try:
            call_command('importdata', file_path, model_name)
            messages.success(request, 'Data is imported sucessfully!')
        except Exception as e:
            messages.error(request, str(e))
            return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/importdata.html', context)
