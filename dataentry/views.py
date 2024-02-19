from django.contrib import messages
from django.core.management import call_command
from django.shortcuts import render, redirect

from awd_main import settings
from dataentry.utils import get_all_custom_models, check_csv_errors
from uploads.models import Upload
from .tasks import import_data_task, export_data_task

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

        #check for the CSV error
        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('import_data')

        #handle the import data task
        import_data_task.delay(file_path, model_name)

        #show the message to the user
        messages.success(request, ('Your data is being imported, you will be notified once it is done.'))
        return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/importdata.html', context)

def export_data(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')
        # call the export data task
        export_data_task.delay(model_name)

        # show message to the user
        messages.success(request, 'Your data is being exported, you will be notified once it is done.')
        return redirect('export_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/exportdata.html', context)
