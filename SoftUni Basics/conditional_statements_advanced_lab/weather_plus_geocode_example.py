import requests

city = input('Enter city name: ')
print('Displaying Weather report for: ' + city)
url = 'https://wttr.in/{}'.format(city)
res = requests.get(url)

print(res.text)

# Phonenumbers
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

number = '+359876292839'

ch_number = phonenumbers.parse(number, 'CH')
print(ch_number)
print(geocoder.description_for_number(ch_number, 'en'))

ch_number = phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(ch_number, 'en'))

ch_number = phonenumbers.parse(number)
time_zone = timezone.time_zones_for_number(ch_number)
print(time_zone)

# Geocode
m = folium.Map(location=[42.68410, 23.31743])
result = 'base_map.html'
m.save(result)
