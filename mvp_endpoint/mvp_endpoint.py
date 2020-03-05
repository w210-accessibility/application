from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from mvp_endpoint.ClientPrediction import *
from mvp_endpoint import db
from mvp_endpoint.models import Pano, PanoFeature, SidewalkSegment2, SidewalkSegment3, SegmentToPano2
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint('mvp_endpoint', __name__)

# add a rule for the index page.
@bp.route('/', methods=['Get'])
def index():
    return '<h1>Hi</h1>'

# add a rule when the page is accessed with a name appended to the site
# URL.
@bp.route('/api/predictions/', methods=['GET'])
def get_data_for_bounding_box():
    # for mapbox, bounding boxes go (SW, NE)
    sw_lat = try_parse_float(request.args.get('lat1'))
    sw_long = try_parse_float(request.args.get('long1'))
    ne_lat = try_parse_float(request.args.get('lat2'))
    ne_long = try_parse_float(request.args.get('long2'))

    results = SidewalkSegment2.query.filter(SidewalkSegment2.startLat >= sw_lat) \
                                    .filter(SidewalkSegment2.startLat <= ne_lat) \
                                    .filter(SidewalkSegment2.startLong >= sw_long) \
                                    .filter(SidewalkSegment2.startLong <= ne_long).all()

    response_geojson = {}
    sidewalk_issues = []
    missing_sidewalk = []

    ## JUST TRYING SOMETHING OUT to simulate the real thing
    ## only showing yellow every 10
    ## red every 45
    for i, result in enumerate(results):
        if i % 45 == 0:
            missing_sidewalk.append(result.geoJson["features"][0])
        if i % 10 == 0:
            sidewalk_issues.append(result.geoJson["features"][0])

    response_geojson["missing_sidewalk"] = missing_sidewalk
    response_geojson["sidewalk_issues"] = sidewalk_issues
    return jsonify(response_geojson)

def try_parse_float(inp):
    try:
        x = float(inp)
    except:
        x = 0
    return x
