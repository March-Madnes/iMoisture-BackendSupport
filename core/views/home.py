import os
import requests
from flask import Blueprint, jsonify, request
from dotenv import load_dotenv

load_dotenv()

home = Blueprint("home", __name__)


@home.route("/api")
def home_latest():
    return jsonify({"message": "Hello Server"})


base_url = os.getenv("BASE_URL")


@home.route("/api/predict", methods=["POST"])
def analyse_soil():
    url = base_url + "/api/predict"
    image = request.files.get("image")
    if image:
        files = {"image": image}
        response = requests.post(url, files=files, verify=False)

        return response.json()

    return "no image found"


@home.route("/api/crop_suggest")
def crop_suggest_api():
    nitrogen = request.args.get("nitrogen", default=30)
    phosphorous = request.args.get("phosphorous", default=90)
    potassium = request.args.get("potassium", default=120)
    ph = request.args.get("ph", default=6)
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    url = base_url + "/api/crop_suggest"
    params = {
        "nitrogen": nitrogen,
        "phosphorous": phosphorous,
        "potassium": potassium,
        "ph": ph,
        "lat": lat,
        "lon": lon,
    }
    response = requests.get(url, params=params, verify=False)
    return response.json()
