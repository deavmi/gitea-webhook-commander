#!/usr/bin/python3.9

from flask import request, Flask
from flask.logging import logging
from flask import render_template

# Setup the Flask web app.
app = Flask("thing")

commands={
        "homepage" : {
                "dir":"/home/pi/HDD/temp/homepage",
                "command":"hugo"
        },
        "crxn" : {
                "dir":""
        }
}

@app.route("/build/<site>", methods=["POST"])
def buildHandler(site):
        from flask import request
        print(request.headers)
        print("Requesting an automatic rebuild of '%s'"%(site))

        item=commands[site]
        itemDir=item["dir"]
        itemCommand=item["command"]

        import subprocess
        import os
        os.chdir(itemDir)
        subprocess.call(itemCommand)

        return "Bruh"
