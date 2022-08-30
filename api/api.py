import os

from flask import Flask

from models.earthquake import EarthquakeModel

app = Flask(__name__)
app.debug = False

AWS_ACCESS_KEY_ID = "DUMMYIDEXAMPLE"
AWS_SECRET_ACCESS_KEY = "DUMMYEXAMPLEKEY"

os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_ACCESS_KEY

EarthquakeModel.create_table(read_capacity_units=1, write_capacity_units=1)


@app.route("/hello_world")
def hello_world():
    return "HelloWorld"


@app.route("/earthquakes")
def fetch_earthquakes():
    earthquakes = EarthquakeModel.scan()
    # earthquakes_str = ','.join(str(earthquake) for earthquake in earthquakes)
    return [e.serialize() for e in earthquakes]


app.run(debug=True)
