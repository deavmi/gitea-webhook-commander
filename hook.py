#!/usr/bin/python3

from flask import request, Flask
from flask.logging import logging
from flask import request
import subprocess
import os
import json

# Setup the Flask web app.
app = Flask("thing")

# Authorization
#
# If set to `None` then authorization
# is ignored
auth=None

# Commands collection
commands={
}

def initAuth():
	global auth
	auth=os.getenv("GITEA_WEBHOOK_AUTH")

def initCommands(file):
    global commands
    commands = json.loads(open(file, "r").read())

@app.route("/build/<site>", methods=["POST"])
def buildHandler(site):
	print("Requesting an automatic rebuild of '%s'"%(site))

	# Extract the auth token
	authHeader=request.headers["Authorization"]

	# Do authorization check
	#
	# (only if auth is enabled ourside,
	# irrespective of how Gitea was configured
	# to send its headers)
	global auth
	if(auth != None and authHeader != auth):
		print("The auth token '%s' doesn't match the configured one"%(authHeader))
		return "Bad"; # FIXME: Return 300?

	if(not (site in commands)):
		print("No configuration for item '%s'"%(site))
		return "Bad"; # FIXME: Return 300?

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

initAuth()
initCommands("commands.json")
app.run(host="::")
