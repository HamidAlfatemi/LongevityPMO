# Create a management command (e.g., update_gene_id_case.py)
from django.core.management.base import BaseCommand
from longevity.models import Genage,Cellage,Requieddata,Signature #,InterventionGene

class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in Genage.objects.all():
            obj.gene_id = obj.Gene_id
            obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated gene_id case.'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in InterventionGene.objects.all():
            obj.gene_id = obj.Gene_id
            obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated gene_id case.'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in Cellage.objects.all():
            obj.gene_id = obj.Gene_id
            obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated gene_id case.'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in Requieddata.objects.all():
            obj.gene_id = obj.Gene_id
            obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated gene_id case.'))

class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in Signature.objects.all():
            obj.gene_id = obj.Gene_id
            obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated gene_id case.'))
