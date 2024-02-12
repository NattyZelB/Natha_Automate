import csv

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError

from dataentry.models import Student


#Proposed command -python manage.py importdata file_path model_name
class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name',type=str, help='Name of the model')
    def handle(self, *args, **kwargs):
        #file path
        file_path = kwargs['file_path']
        model_name = kwargs['model_name']

        #Search for the model access all inserted
        model = None
        for app_config in apps.get_app_configs():
            # Try to search for the model inside the apps
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found.
            except LookupError:
                continue # model not found in this app, continue searching in next app.

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')
        #for open file
        with open(file_path, 'r')as file:
        #read from CSV file
            reader = csv.DictReader(file)
            for row in reader:
                #**row for inport data from row
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Data import from CSV successfully!"))
