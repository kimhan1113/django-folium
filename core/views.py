from django.shortcuts import render
from django.db.models import Avg
import folium
from folium.plugins import FastMarkerCluster
from core.models import EVChargingLocation, KoreaCitiesLocation

# Create your views here.
def index(request):

    # stations = EVChargingLocation.objects.all()

    cities = KoreaCitiesLocation.objects.all()

    # avg_lat = EVChargingLocation.objects.aggregate(avg=Avg('latitude'))['avg']

    # stations= EVChargingLocation.objects.filter(latitude__gt=avg_lat)
    # stations= EVChargingLocation.objects.exclude(latitude__gt=avg_lat)




    # m = folium.Map(location=[41.5025, -72.699997], zoom_start=9)


    m = folium.Map(location=[37.56, 126.99], zoom_start=9)


    for city in cities:
        coordinates = (city.latitude, city.longitude)
        folium.Marker(coordinates, popup=city.city_name).add_to(m)


    # for station in stations:
    #     coordinates = (station.latitude, station.longitude)
    #     folium.Marker(coordinates, popup=station.station_name).add_to(m)

    
    # latitudes = [station.latitude for station in stations]
    # longtitudes = [station.longitude for station in stations]

    # FastMarkerCluster(data=list(zip(latitudes, longtitudes))).add_to(m)

    context = {'map': m._repr_html_()}

    return render(request, 'index.html', context)