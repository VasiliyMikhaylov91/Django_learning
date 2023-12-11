from django.core.management.base import BaseCommand
from myapp.models import Item


class Command(BaseCommand):
    help = "Fill Item table."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            item = Item(name=f'item{i}', description=f'Something about item{i}',
                        price=100*i, count=i)
            item.save()
            self.stdout.write(f'{item}')
