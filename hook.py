#!/usr/bin/python3.9

from flask import request, Flask
from flask.logging import logging
from flask import request
import subprocess
import os
import json

# Setup the Flask web app.
app = Flask("thing")

commands={
}

def initCommands(file):
    global commands
    commands = json.loads(file)

@app.route("/build/<site>", methods=["POST"])
def buildHandler(site):
	print("Requesting an automatic rebuild of '%s'"%(site))

	# Extract the correct mapping
	item=commands[site]
	itemDir=item["dir"]
	itemPreCommand=item["pre-command"]
	itemCommand=item["command"]

	# Change directory to the item's CWD
	os.chdir(itemDir)

	# Call the pre-command followed by the command
	subprocess.call(itemPreCommand)
	subprocess.call(itemCommand)

	# The deadline will probably be exceeded but flask
	# wants this here
	return "Ok"

initCommands("commands.json")
app.run(host="fdd2:cbf2:61bd::2")
