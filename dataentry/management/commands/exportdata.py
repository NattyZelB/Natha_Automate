import csv
from django.core.management.base import BaseCommand
from dataentry.models import Student
from django.apps import apps

from dataentry.utils import generate_csv_file


# proposed command= python manage.py exportdata
class Command(BaseCommand):
    help = 'Export data from Student model to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')
    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        #search though all the installed apps for the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop executing once the model is found.
            except LookupError:
                pass

        if not model:
            self.stderr.write(f'Model {model_name} could not find!')
            return

        # feth the data from the database
        data = model.objects.all()

        #generate csv file_path
        file_path = generate_csv_file(model_name)


        #print(file_path)
        # open the csv file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            #write the CSV header
            #we want to print the field names of the model that we try to export
            writer.writerow([field.name for field in model._meta.fields])

            #write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))