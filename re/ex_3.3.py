"""Спарсить значение lon и lat из файла map.xml"""
import re

with open("re/map.xml", "r") as file_object:
    lon = []
    lat = []
    for text in file_object:
        match = re.findall(r"<point\s+[^>]*?lon=([\"\'])([0-9.,]+)\1\s+[^>]*lat=\1([0-9.,]+)\1", text)
        if len(match) > 0:
            lon.append(match[0][1])
            lat.append(match[0][2])
    
    print(lon, lat, sep="\n")