"""Спарсить значение lon и lat из файла map.xml"""
import re

with open("re/map.xml", "r") as file_object:
    lon = []
    lat = []
    for text in file_object:
        match = re.search(r"<point\s+[^>]*?lon=([\"\'])(?P<lon>[0-9.,]+)\1\s+[^>]*lat=\1(?P<lat>[0-9.,]+)\1", text)
        if match:
            v = match.groupdict()
            if "lon" in v and "lat" in v:
                lon.append(v["lon"])
                lat.append(v["lat"])
    
    print(lon, lat, sep="\n")