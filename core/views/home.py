import requests
from flask import Blueprint, jsonify, request

home = Blueprint("home", __name__)


@home.route("/api")
def home_latest():
    return jsonify({"message": "Hello Server"})


@home.route("/api/predict", methods=["POST"])
def analyse_soil():
    url = "https://54.174.69.218/api/predict"
    image = request.files.get("image")
    if image:
        files = {"image": image}
        response = requests.post(url, files=files, verify=False)

        return response.json()

    return "no image found"


@home.route("/api/crop_suggest")
def crop_suggest_api():
    url = "https://54.174.69.218/api/crop_suggest"
    response = requests.get(url, verify=False)
    return response.json()
