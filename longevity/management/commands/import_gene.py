from django.conf import settings

import csv
import sys
import os
project_root = r'C:\lpmo\lpmo'
sys.path.append(project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lpmo.settings')

from django.core.management.base import BaseCommand
from django.conf import settings
from longevity.models import Gene

class Command(BaseCommand):
    help = 'Import data from CSV files into Gene model'

    def add_arguments(self, parser):
        parser.add_argument('gene_csv', help='Path to the Gene CSV file')

    def handle(self, *args, **kwargs):
        base_dir = settings.BASE_DIR
        gene_csv_path = os.path.join(base_dir, kwargs['gene_csv'])

        # Import data into Gene model
        with open(gene_csv_path, 'r') as gene_csv_file:
            csv_reader = csv.DictReader(gene_csv_file)
            #print(f"CSV Headers: {headers}")
            for row in csv_reader:
                gene = Gene(
                    gsymbol=row['gsymbol'],
                )
                gene.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
