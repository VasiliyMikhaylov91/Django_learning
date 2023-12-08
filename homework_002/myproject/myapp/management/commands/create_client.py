from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        client = Client(name='John', email='john@example.com',
                    tel='12345', address='somewhere')
        client.save()
        self.stdout.write(f'{client}')
