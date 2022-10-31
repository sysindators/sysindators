import phonenumbers, opencage, folium, os, geocoder

from phonenumbers import geocoder as geonumber
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
from sys import exit as logout
from clear_cache import clear as clear_cache


def PhoneNumber(number):
    pepnumber = phonenumbers.parse(number)
    location = geonumber.description_for_number(pepnumber, "en")
    service_pro = phonenumbers.parse(number)
    key = "eb5422d94366466dadc76b5c7ced1bc1"
    data = OpenCageGeocode(key)
    query = str(location)
    results = data.geocode(query)
    print(f"\n > Location : {location}")
    print(" > Name : " + carrier.name_for_number(service_pro, "en"))
    # print(f" > Results : {results}")

    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]

    print(f" > Lat : {lat}")
    print(f" > Lng : {lng}")

    Map = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(Map)

    Map.save("location.html")
    print(" > File :  location.html")
    print(
        "\n[!] Run the location.html file to see the location of the phone number you are looking for\n"
    )
    clear_cache(dir=".")
    logout()


def Ip(ip):
    g = geocoder.ip(ip)
    address = g.latlng
    Map = folium.Map(location=address, zoom_start=12)
    folium.CircleMarker(location=address, radius=50, popup=ip).add_to(Map)
    folium.Marker(address, popup=ip).add_to(Map)
    Map.save("location.html")
    print(f"\n > IP Address : {ip}")
    print(f" > Lat and Lng : {address}")
    print(" > File :  location.html")
    print(
        "\n[!] Run the location.html file to see the location of the IP Address you are looking for\n"
    )
    clear_cache(dir=".")
    logout()
