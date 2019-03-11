from django.core.management.base import BaseCommand

from shiptrader.utils import StrashipsImporter


class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Start reading and processing straships data'))
        processor = StrashipsImporter()
        processor.read_process_data()
        self.stdout.write(self.style.SUCCESS(
            'Reading and processing straships data has been successful'))

