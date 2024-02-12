from django.core.management.base import BaseCommand

from dataentry.models import Student


#I want to add some data to the database using the custom command
class Command(BaseCommand):
    help = 'It will insert data to data the database'

    def handle(self, *args, **kwargs):
    # logic goes hier
        dataset = [
            {'roll_no':1002, 'name': 'Vincent', 'age':20 },
            {'roll_no': 1005, 'name': 'Alice', 'age': 20},
            {'roll_no': 1006, 'name': 'Mark', 'age': 20},
            {'roll_no': 1007, 'name': 'Aalyza', 'age': 19},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING("Student with this rol no is already exists!"))

        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
