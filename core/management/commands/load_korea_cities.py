
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import EVChargingLocation, KoreaCitiesLocation


class Command(BaseCommand):
    help = 'Load data from korea cities'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / 'korea_cities.csv'
        
        # with open(data_file, 'rt', encoding='UTF8') as csvfile:
        with open(data_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            # for row in reader:
            #     records.append({k: row[k] for k in keys})

        # print()

        # extract the latitude and longitude from the Point object
            for record in reader:
                # print(record['city'], record['lat'], record['lat'])
                # assert 1==0
                # add the data to the database
                KoreaCitiesLocation.objects.get_or_create(
                    city_name=record['city'],
                    latitude=record['lat'],
                    longitude=record['lng']
                )