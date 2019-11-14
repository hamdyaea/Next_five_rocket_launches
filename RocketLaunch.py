#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com
#
# This Python3 software print in the terminal the next five rocket launch. The data is updated at every run.


import json
import urllib.request


def main():
    urlData = "https://launchlibrary.net/1.4/launch/next/5"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset("utf-8")
    launch = json.loads(data.decode(encoding))

    print("\n--- Next five rocket launches ---\n\n")
    try:
        print(("Name : ") + str(launch["launches"][0]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(launch["launches"][0]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(("Start time : ") + str(launch["launches"][0]["windowstart"]) + str("\n"))
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(launch["launches"][1]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(launch["launches"][1]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(("Start time : ") + str(launch["launches"][1]["windowstart"]) + str("\n"))
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(launch["launches"][2]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(launch["launches"][2]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(("Start time : ") + str(launch["launches"][2]["windowstart"]) + str("\n"))
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(launch["launches"][3]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(launch["launches"][3]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(("Start time : ") + str(launch["launches"][3]["windowstart"]) + str("\n"))
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    try:
        print(("Name : ") + str(launch["launches"][4]["name"]) + str("\n"))
    except:
        print(("Name : ") + str("no name"))
        pass
    try:
        print(
            ("Description : ")
            + str(launch["launches"][4]["missions"][0]["description"])
            + str("\n")
        )
    except:
        print(("Description : ") + str("no description") + str("\n"))
    try:
        print(("Start time : ") + str(launch["launches"][4]["windowstart"]) + str("\n"))
    except:
        print(("Start time : ") + str("no windowstart") + str("\n"))
    print("\n\n")
    print("Developer - Author : Hamdy Abou El Anein\nhttps://github.com/hamdyaea")


main()
