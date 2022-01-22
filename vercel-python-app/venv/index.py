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
        req = Request("https://astrometry.ch/rockets.json", headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req,timeout=10).read()
        Rocketlaunch = json.loads(data.decode())
        rocketlist = []
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
                mission = i["mission"]["name"]
            except:
                mission = ""
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
        
            rocketlist.append(str("<p><strong>Spacecraft     </strong>")+str(spacecraft)+str("<br><strong>Type     </strong>")+str(type)+str("<br><strong>Launch time     </strong>")+str(time)+str("<br><strong>Rocket company     </strong>")+str(company)+str("<br><strong>Reason     </strong>")+str(mission)+str("<br><strong>Description     </strong>")+str(description)+str("<br><strong>Orbit     </strong>")+str(orbit)+str("</p>")+str('<img src=\"')+str(pic)+str('\" alt=\"Rocket picture\" align=\"left\" style=\"width:400px;height:300px;">')+str("<br><br><br><br><br><br><br><br><br><br><br><br><br>"))
        
        num = Rocketlaunch["count"]
        return render_template("index.html",num=num,rocketlist=rocketlist)
    except:
        num = 0
        rocketlist = ["<strong>Too many requests, please try later...</strong>"]
        return render_template("index.html",num=num,rocketlist=rocketlist)
