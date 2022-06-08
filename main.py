from flask import Flask, render_template, make_response, request, redirect, url_for
import requests
import json
import os
import time
import compress_json
import addfips
from zipfile import ZipFile
import csv

from Dispatcher import Dispatcher

global THIS_FOLDER
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
global CITY_NAME
CITY_NAME = ""

app = Flask("__main__", template_folder=os.path.join(THIS_FOLDER, "templates"))

@app.route("/")
@app.route("/choose_city")
def choosecity():
    html = render_template("choose_city.html")
    response = make_response(html)
    return response


@app.route("/setup")
def setup():
    html = render_template("setup.html")
    response = make_response(html)
    return response

# TODO: Does not work for multi-polygons yet
@app.route("/setup-interactive")
def setup_interactive():
    token = 'pk.eyJ1IjoiZ2xhbmlld3NraSIsImEiOiJja28weW13eHEwNWNwMnZzNTZyZzRrMDN4In0.P2-EylpYdzmCgdASgAKC5g'
    jawg_accessToken = 'uUILlBVmedZhJqrmWPczZMS9ytaAuTPvGqX5Z3bCC30qlHe2DSJCQZABdbznjyGr'
    #r = requests.get('https://raw.githubusercontent.com/whosonfirst-data/whosonfirst-data-admin-us/master/data/859/401/95/85940195.geojson')
    #print(r.json()['geometry']['coordinates'])
    html = render_template("setup-interactive.html", mapbox_access_token = token, jawg_accessToken = jawg_accessToken)
    response = make_response(html)
    return response


@app.route("/create_animation", methods=['POST'])
def create_animation():
    global CITY_NAME
    CITY_NAME = request.args.get('city_name')
    county_name = request.args.get('county_name')
    state_name = request.args.get('state_name')
    url_path = request.args.get('url_path')
    list_kiosks = request.args.get('list_kiosks').split(',')
    list_kiosks = [[int(name), float(lat), float(lon)] for name, lat, lon in [list_kiosks[x:x+3] for x in range(0, len(list_kiosks), 3)]]
    print(CITY_NAME, county_name, state_name, url_path, list_kiosks)

    af = addfips.AddFIPS()
    fips_code = af.get_county_fips(county_name, state=state_name)
    global THIS_FOLDER
    for filename in os.listdir(os.path.join(THIS_FOLDER, "local_static", "StateTripFiles_Compressed")):
        if state_name.replace(" ", "") in filename:
            filepath = os.path.join(THIS_FOLDER, "local_static", "StateTripFiles_Compressed", filename)
            print(filepath)
            with ZipFile(filepath, 'r') as f:
                list_of_zipped_files = ZipFile.namelist(f)
                list_of_files_to_unzip = [filename for filename in list_of_zipped_files if fips_code in filename]
                f.extractall(os.path.join(THIS_FOLDER, "local_static"), members = list_of_files_to_unzip)
            break

    depot_data_filename = CITY_NAME+"_AV_STATION.csv"
    fields = ["Name", "Lat", "Long"]
    with open(os.path.join(THIS_FOLDER, "local_static", depot_data_filename), 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(list_kiosks)


    start_time = time.time()
    global THIS_FOLDER
    input_datafeed_depot_data = os.path.join(THIS_FOLDER, "local_static", depot_data_csv)
    input_datafeed_trip_data = []
    for trip_data_csv in lst_trip_data_csv:
        input_datafeed_trip_data.append("local_static/" + trip_data_csv)

    print(input_datafeed_trip_data)
    print("MODESPLIT:", modesplit)
    print(min_lat, max_lat, min_lng, max_lng)

    lst_passengers_left = []

    aDispatcher = Dispatcher(CITY_NAME, angry_passenger_threshold_sec)
    aDispatcher.createDataFeed(input_datafeed_depot_data, input_datafeed_trip_data, min_lat, max_lat, min_lng, max_lng, modesplit)

    for idx, fleetsize in enumerate(lst_fleetsize):
        print("Fleetsize:", fleetsize)
        aDispatcher.resetDataFeed()
        aDispatcher.createNumVehicles(fleetsize)
        index_metrics, trips, depot_locations, missed_passengers, waiting, metrics, metric_animations, last_arrival_at_depot_time, looplength, runtime = aDispatcher.solve()
        passengers_left = index_metrics[1]
        lst_passengers_left.append(passengers_left)
        print("MISSED PASSENGERS:", passengers_left)
        if (passengers_left == 0) or (idx == len(lst_fleetsize)-1):
            print("DONE, PRINTING RESULTS")
            # Write to files
            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "index_metrics.txt")
            with open(my_file, "w") as f:
                index_metrics.append(fleetsize)
                f.write(str(index_metrics))

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "looplength.txt")
            with open(my_file, "w") as f:
                f.write(str(looplength))

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "trips.json.gz")
            compress_json.dump(trips, my_file)

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "depot_locations.txt")
            with open(my_file, "w") as f:
                f.write(str(depot_locations))

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "missed_passengers.json.gz")
            compress_json.dump(missed_passengers, my_file)

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "waiting.json.gz")
            compress_json.dump(waiting, my_file)

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "metrics.json.gz")
            compress_json.dump(metrics, my_file)

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "metric_animations.json.gz")
            compress_json.dump(metric_animations, my_file)

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "looplength.txt")
            with open(my_file, "w") as f:
                f.write(str(looplength))

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "runtime.txt")
            with open(my_file, "w") as f:
                f.write(str(runtime))

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "pax_left_vs_fleetsize.txt")
            with open(my_file, "w") as f:
                f.write(str([lst_fleetsize, lst_passengers_left]))

            my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "viewstate_coordinates.txt")
            with open(my_file, "w") as f:
                avg_lat = (min_lat + max_lat)/2
                avg_lng = (min_lng + max_lng)/2
                f.write(str([avg_lat, avg_lng]))

            break

    html = render_template("create_animation.html", run_time=time.time()-start_time)
    response = make_response(html)
    return response

@app.route("/animation")
def my_index():
    global THIS_FOLDER
    global CITY_NAME
    CITY_NAME = request.args.get('city_choice', default = CITY_NAME)
    animation_speed = request.args.get('animation_speed', default = 1, type = int)
    start_time = request.args.get('start_time', default = 0, type = int)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "depotbuildings.csv")
    with open(my_file, "r") as f:
        buildings = json.load(f)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "trips.json.gz")
    trips = compress_json.load(my_file)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "depot_locations.txt")
    with open(my_file, "r") as f:
        depot_locations = f.read()

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "missed_passengers.json.gz")
    missed_passengers = compress_json.load(my_file)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "waiting.json.gz")
    waiting = compress_json.load(my_file)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "metric_animations.json.gz")
    metric_animations = compress_json.load(my_file)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "looplength.txt")
    with open(my_file, "r") as f:
        loop_length = int(f.read())

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "index_metrics.txt")
    with open(my_file, "r") as f:
        index_metrics = f.read()

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "metrics.json.gz")
    metrics = compress_json.load(my_file)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "viewstate_coordinates.txt")
    with open(my_file, "r") as f:
        viewstate_coordinates = f.read()

    html = render_template("index.html", buildings=buildings, trips = trips, depot_locations = depot_locations, missed_passengers = missed_passengers, waiting = waiting, metric_animations = metric_animations, loop_length = loop_length, animation_speed=animation_speed, start_time=start_time, metrics = metrics, index_metrics = index_metrics, viewstate_coordinates=viewstate_coordinates)
    response = make_response(html)
    return response


@app.route("/graphs")
def graph_page():
    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "metrics.json.gz")
    metrics = compress_json.load(my_file)

    my_file = os.path.join(THIS_FOLDER, "static", CITY_NAME, "pax_left_vs_fleetsize.txt")
    with open(my_file, "r") as f:
        pax_left_vs_fleetsize_data = f.read()

    html = render_template("graphs.html", metrics = metrics, pax_left_vs_fleetsize_data = pax_left_vs_fleetsize_data)
    response = make_response(html)
    return response

#Comment out before updating PythonAnywhere
app.run()
