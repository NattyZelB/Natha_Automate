from django.core.management.base import BaseCommand

class Command(BaseCommand):
     help = 'Greets the user'

     #parser use for replace word.
     def add_arguments(self, parser):
        parser.add_argument('name',type=str, help='Specifies user name')

     def handle(self, *args, **kwargs):
        #write the logic
        name = kwargs['name']
        greeting = f'Hi {name},How are you?'
        self.stdout.write(self.style.SUCCESS(greeting))