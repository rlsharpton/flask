from flask import Flask
from flask import render_template
import os
import json
import time
import urllib2

app = Flask(__name__)

"""
@app.route("/")
def index():
	return "Hello World";

@app.route("/goodbye")
def goodbye():
	return "Goodby, World!"

@app.route("/hello/<name>")
def hello_name(name):
	return "Hello, {}".format(name)
"""
def get_weather():
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?=London&mode=json&units=metric"
	response = urllib2.urlopen(url).read()
	return response

@app.route("/")
def index():
	data = json.loads(get_weather())
	day = time.strftime('%d %B', time.localtime(data.get('list')[0].get('dt')))
	mini = data.get("list")[0].get("temp").get("min")
	maxi = data.get("list")[0].get("temp").get("max")
	description = data.get("list")[0].get("weather")[0].get("description")
	return render_template("index.html", day=day, mini=mini, maxi=maxi, description=description)



if __name__ ==  '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port, debug=True)
