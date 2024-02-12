from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Print Hello world'

    def handle(self, *args, **kwargs):
    # we write the logic
    # testing git
        self.stdout.write("Hi Natty, How are you?")