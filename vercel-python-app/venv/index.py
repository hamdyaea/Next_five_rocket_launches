#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# This Python3 software print in the terminal the next five rocket launch. The data is updated at every run.

from flask import Flask, render_template
from urllib.request import Request, urlopen
import json

app = Flask(__name__)

@app.route("/")
def main():
    try:
        req = Request("https://ll.thespacedevs.com/2.2.0/launch/?format=json&last_updated__gte=&last_updated__lte=&mission__orbit__name=&mission__orbit__name__icontains=&name=&net__gt=&net__gte=&net__lt=&net__lte=&r_spacex_api_id=&rocket__configuration__full_name=&rocket__configuration__full_name__icontains=&rocket__configuration__id=&rocket__configuration__manufacturer__name=&rocket__configuration__manufacturer__name__icontains=&rocket__configuration__name=&rocket__spacecraftflight__spacecraft__id=&rocket__spacecraftflight__spacecraft__name=&rocket__spacecraftflight__spacecraft__name__icontains=&slug=&status=1&window_end__gt=&window_end__gte=&window_end__lt=&window_end__lte=&window_start__gt=&window_start__gte=&window_start__lt=&window_start__lte=", headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req,timeout=10).read()
        Rocketlaunch = json.loads(data.decode())
        rocketlist = []
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
        
            rocketlist.append(str("<p><strong>Spacecraft     </strong>")+str(spacecraft)+str("<br><strong>Type     </strong>")+str(type)+str("<br><strong>Launch time     </strong>")+str(time)+str("<br><strong>Rocket company     </strong>")+str(company)+str("<br><strong>Reason     </strong>")+str(mission)+str("<br><strong>Description     </strong>")+str(description)+str("<br><strong>Orbit     </strong>")+str(orbit)+str("</p>")+str('<img src=\"')+str(pic)+str('\" alt=\"Rocket picture\" align=\"left\" style=\"width:400px;height:300px;">')+str("<br><br><br><br><br><br><br><br><br><br><br><br><br>"))
        
        num = Rocketlaunch["count"]
        return render_template("index.html",num=num,rocketlist=rocketlist)
    except:
        num = 0
        rocketlist = ["<strong>Too many requests, please try later...</strong>"]
        return render_template("index.html",num=num,rocketlist=rocketlist)
