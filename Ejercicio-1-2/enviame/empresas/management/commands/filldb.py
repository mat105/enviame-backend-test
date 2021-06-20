from django.core.management import BaseCommand
from model_bakery import baker

from empresas.models import Company


class Command(BaseCommand):
    help = 'Fills the db with [x] ammount of objects'

    def add_arguments(self, parser):
        parser.add_argument('--companies', type=int, help='Ammount of companies to create (default 10)', default=10)

    def handle(self, *args, **options):
        companies_quantity = options['companies']

        if companies_quantity > 0:
            baker.make(Company, _quantity=companies_quantity)
