#OxygenDB is a web based database specifically made to coordinate the data flow and distribution of a small project but feel welcome to use/modify it to fit your needs
import os.path
from flask import Flask
from flask import request
app = Flask("__name__")

@app.route("/")
def hello():
	return "OxygenDB is a web based database specifically made to coordinate the data flow and distribution of a small project but feel welcome to use/modify it to fit your needs"

@app.route("/read/<document>/<apikey>")
def readdoc(document, apikey):
	if os.path.isfile("clients/" + apikey):
		if os.path.isfile("data/" + document):
			fdoc = open("data/" + document, "r")
			rdoc = fdoc.read()
			return rdoc
		else:
			return "Document not found"
	else:
		return "Missing/Incorrect API authentication token"

@app.route("/create/<document>/<apikey>")
def createdoc(document, apikey):
	if os.path.isfile("clients/" + apikey):
		if os.path.isfile("data/" + document):
			return "Document already exists"
		else:
			newfile = open("data/" + document, "w")
			return "Document succesfully created"
	else:
		return "Missing/Incorrect API authentication token"

@app.route("/delete/<document>/<apikey>")
def deletedoc(document, apikey):
	if os.path.isfile("clients/" + apikey):
		if os.path.isfile("data/" + document):
			os.remove("data/" + document)
			return "Document succesfully deleted"
		else:
			return "Document not found"
	else:
		return "Missing/Incorrect API authentication token"

@app.route("/write/<document>/<data>/<apikey>")
def writedoc(document, apikey, data):
	if os.path.isfile("clients/" + apikey):
		if os.path.isfile("data/" + document):
			writefile = open("data/" + document, "w")
			writefile.write(data)
			return "Document succesfully updated"
		else:
			return "Document not found"
	else:
		return "Missing/Incorrect API authentication token"
