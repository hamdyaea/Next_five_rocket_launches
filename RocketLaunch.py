#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com

# This Python3 software print in the terminal the next five rocket launch. The data is updated at every run.


class Rocket:
    def __init__(self):
        self.launch


import json
import urllib.request


def main():
    urlData = "https://launchlibrary.net/1.4/launch/next/5"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset("utf-8")
    Rocket.launch = json.loads(data.decode(encoding))
    print(
        "  _   _           _     _____   _____            _        _     _                            _ "
    )
    print(
        " | \ | |         | |   | ____| |  __ \          | |      | |   | |                          | |"
    )
    print(
        " |  \| | _____  _| |_  | |__   | |__) |___   ___| | _____| |_  | |     __ _ _   _ _ __   ___| |__ "
    )
    print(
        " | . ` |/ _ \ \/ / __| |___ \  |  _  // _ \ / __| |/ / _ \ __| | |    / _` | | | | '_ \ / __| '_ \ "
    )
    print(
        " | |\  |  __/>  <| |_   ___) | | | \ \ (_) | (__|   <  __/ |_  | |___| (_| | |_| | | | | (__| | | | "
    )
    print(
        " |_| \_|\___/_/\_\\__|  |____/  |_|  \_\___/ \___|_|\_\___|\__| |______\__,_|\__,_|_| |_|\___|_| |_|"
    )

    print("\n--- Next five rocket launches ---\n\n")
    try:
        print(("Name : ") + str(Rocket.launch["launches"][0]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(Rocket.launch["launches"][0]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(
            ("Start time : ")
            + str(Rocket.launch["launches"][0]["windowstart"])
            + str("\n")
        )
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(Rocket.launch["launches"][1]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(Rocket.launch["launches"][1]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(
            ("Start time : ")
            + str(Rocket.launch["launches"][1]["windowstart"])
            + str("\n")
        )
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(Rocket.launch["launches"][2]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(Rocket.launch["launches"][2]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(
            ("Start time : ")
            + str(Rocket.launch["launches"][2]["windowstart"])
            + str("\n")
        )
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(Rocket.launch["launches"][3]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(Rocket.launch["launches"][3]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(
            ("Start time : ")
            + str(Rocket.launch["launches"][3]["windowstart"])
            + str("\n")
        )
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(Rocket.launch["launches"][4]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(Rocket.launch["launches"][4]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(
            ("Start time : ")
            + str(Rocket.launch["launches"][4]["windowstart"])
            + str("\n")
        )
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    print("Developer - Author : Hamdy Abou El Anein\nhttps://github.com/hamdyaea")


main()
