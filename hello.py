from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hellow World testing</p>"

@app.route("/country/")
def getCountry():
  url = 'https://restcountries.com/v3.1/all'
  r = requests.get(url)
  return r.content

@app.route("/country/<name>")
def getCountryByName(name):
  url = 'https://restcountries.com/v3.1/name/'+name
  r = requests.get(url)
  return r.content