from django.core.management.base import BaseCommand
from ._sample_data2 import createSample, Sample1

class Command(BaseCommand):
    help = "populate database with sample data"

    def handle(self, *args, **options):
        createSample(Sample1)
        
