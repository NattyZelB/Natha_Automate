import csv

from django.apps import apps
from django.core.management.base import BaseCommand, CommandError
from django.db import DataError

from dataentry.models import Student


#Proposed command -python manage.py importdata file_path model_name
class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')
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

        # compare csv header with model's field name
        #get the field name of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        print(model_fields)

        #for open file
        with open(file_path, 'r')as file:
        #read from CSV file
            reader = csv.DictReader(file)
        # we don't want another filed name that in their field.
            csv_header = reader.fieldnames

        # compare csv header with model's filed name
            if csv_header != model_fields:
                raise DataError(f"CSV file doesn't match with the {model_name} table fields")
            for row in reader:
                #**row for inport data from row
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS("Data import from CSV successfully!"))
