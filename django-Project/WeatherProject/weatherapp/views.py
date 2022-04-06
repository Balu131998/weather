from django.shortcuts import render
from .models import Point
import geocoder
import folium
import requests
from django.contrib.gis.geos import fromstr
import json
# Create your views here.
def weather(request):
    if request.method=="POST":
        address=request.POST['city']
        print(address)
        location=geocoder.osm(address)
        url='https://api.openweathermap.org/data/2.5/weather?q=' + address + '&units=metric&appid=e325f6e4580dbda483dc8c54a0466212'
        r=requests.get(url.format(address))
        y=r.json()
        lat=y['coord']['lat']
        lon=y['coord']['lon']
        temp=y['main']['temp']
        humidity=y['main']['humidity']
        Data=('lat',lat,'lon',lon,'humidity',humidity,'temp',temp)
        print(r.text)
        MAP=folium.Map(location=(lat,lon), zoom_start=10)
        folium.Marker((lat,lon),tooltip="CLICK FOR MORE",popup=Data).add_to(MAP)
        MAP=MAP._repr_html_()
        b=Point.objects.create(address=address, Location=fromstr("POINT(%s %s)" % (lat, lon), srid=4326),humidity=humidity,Temperature=temp)
        b.save()
        context={
            'MAP':MAP,
            'lat':lat,
            'lon':lon,
            'humidity':humidity,
            'temp':temp,

        }
        return render(request, 'home.html',context)
    return render(request,'home.html')