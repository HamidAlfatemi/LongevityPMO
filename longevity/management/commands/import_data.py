from django.conf import settings
import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from longevity.models import Node, Edge

class Command(BaseCommand):
    help = 'Import data from CSV files into Node and Edge models'

    def add_arguments(self, parser):
        parser.add_argument('node_csv', help='Path to the Node CSV file')
        parser.add_argument('edge_csv', help='Path to the Edge CSV file')

    def handle(self, *args, **kwargs):
        base_dir = settings.BASE_DIR
        #node_csv_path = kwargs['node_csv']
        #edge_csv_path = kwargs['edge_csv']
        node_csv_path = os.path.join(base_dir, kwargs['node_csv'])
        edge_csv_path = os.path.join(base_dir, kwargs['edge_csv'])

        # Import data into Node model
        with open(node_csv_path, 'r') as node_csv_file:
            csv_reader = csv.DictReader(node_csv_file)
            #print(f"CSV Headers: {headers}")
            for row in csv_reader:
                node = Node(
                    node_id=int(row['node_id']),
                    ref_num=row['ref_num'],
                    nodecaption=row['nodecaption'],
                    nodeshape=int(row['nodeshape']),
                    dash=int(row['dash']),
                    nodecolor=int(row['nodecolor']),
                    container=int(row['container']),
                )
                node.save()

        # Import data into Edge model
        with open(edge_csv_path, 'r') as edge_csv_file:
            csv_reader = csv.DictReader(edge_csv_file)
            for row in csv_reader:
                edge = Edge(
                    #edge_id=row['edge_id'],
                    begin_id=int(row['begin_id']),
                    end_id=int(row['end_id']),
                    edgeshape=int(row['edgeshape']),
                    color=int(row['color']),
                    edgetype=int(row['edgetype']),
                )
                edge.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
