#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# This Python3 software print in the terminal the next five rocket launch. The data is updated at every run.

from urllib.request import Request, urlopen
import json


def main():
    req = Request("https://ll.thespacedevs.com/2.2.0/launch/?format=json&last_updated__gte=&last_updated__lte=&mission__orbit__name=&mission__orbit__name__icontains=&name=&net__gt=&net__gte=&net__lt=&net__lte=&r_spacex_api_id=&rocket__configuration__full_name=&rocket__configuration__full_name__icontains=&rocket__configuration__id=&rocket__configuration__manufacturer__name=&rocket__configuration__manufacturer__name__icontains=&rocket__configuration__name=&rocket__spacecraftflight__spacecraft__id=&rocket__spacecraftflight__spacecraft__name=&rocket__spacecraftflight__spacecraft__name__icontains=&slug=&status=1&window_end__gt=&window_end__gte=&window_end__lt=&window_end__lte=&window_start__gt=&window_start__gte=&window_start__lt=&window_start__lte=", headers={'User-Agent': 'Mozilla/5.0'})
    data = urlopen(req,timeout=10).read()
    Rocketlaunch = json.loads(data.decode())
    for i in Rocketlaunch["results"]:
        spacecraft = i["rocket"]["configuration"]["full_name"]
        type = i["launch_service_provider"]["type"]
        time = i["net"]
        company = i["launch_service_provider"]["name"]
        pic = i["image"] 
        mission = i["mission"]["name"]
        description = i["mission"]["description"]
        type = i["mission"]["type"]
        orbit = i["mission"]["orbit"]["name"]
 
        print(spacecraft)
        print(type)
        print(time)
        print(company)
        print(pic)
        print(mission)
        print(description)
        print(type)
        print(orbit)
        print("\n")

    num = Rocketlaunch["count"]
    print("Number of Rockets")
    print(num)


main()
