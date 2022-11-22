#!/usr/bin/python3.9

from flask import request, Flask
from flask.logging import logging
from flask import request
import subprocess
import os

# Setup the Flask web app.
app = Flask("thing")

commands={
	"homepage" : {
		"dir": "/home/pi/HDD/temp/homepage",
		"pre-command": ["git", "pull"],
		"command": ["hugo"]
	},
	"crxn" : {
		"dir": "/home/pi/HDD/temp/crxn",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/crxn"]
	},
	"bnet": {
		"dir": "/home/pi/HDD/temp/bnet",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/bonobonet"]
	},
	"libtun": {
		"dir": "/home/pi/HDD/temp/libtun",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/libtun"]
	},
	"dlog": {
		"dir": "/home/pi/HDD/temp/dlog",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/dlog"]
	},
	"eventy": {
		"dir": "/home/pi/HDD/temp/eventy",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/eventy"]
	},
	"tasky": {
		"dir": "/home/pi/HDD/temp/tasky",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/tasky"]
	},
	"dnet": {
		"dir": "/home/pi/HDD/temp/dnet",
		"pre-command": ["git", "pull"],
		"command": ["mkdocs", "build", "-d", "/home/pi/HDD/projects/dnet"]
	}
}

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

app.run(host="::")
