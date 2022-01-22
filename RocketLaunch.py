#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# This Python3 software print in the terminal the next rockets launch. The data is updated at every run.

from urllib.request import Request, urlopen
import json


def main():
    req = Request("https://astrometry.ch/rockets.json", headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(req,timeout=10).read()
    Rocketlaunch = json.loads(data.decode())
    for i in Rocketlaunch["results"]:
        try:
            spacecraft = i["rocket"]["configuration"]["full_name"]
        except:
            spacecraft = ""
        try:
            type = i["launch_service_provider"]["type"]
        except:
            type = ""
        try:        
            time = i["net"]
        except:
            time = ""
        try:
            company = i["launch_service_provider"]["name"]
        except:
            company = ""
        try:
            pic = i["image"] 
        except:
            pic = ""       
        try:
            mission1 = i["mission"]["name"]
        except:
            mission1 = ""
        try:
            description = i["mission"]["description"]
        except:
            description = ""
        try:
            type = i["mission"]["type"]
        except:
            type = ""       
        try:        
            orbit = i["mission"]["orbit"]["name"]
        except:
            orbit = ""
        print(spacecraft)
        print(type)
        print(time)
        print(company)
        print(pic)
        print(mission1)
        print(description)
        print(type)
        print(orbit)
        print("\n")

    num = Rocketlaunch["count"]
    print("Number of Rockets")
    print(num)


main()
