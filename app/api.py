#!/usr/bin/env python3

from flask import Blueprint, render_template, abort, jsonify

api = Blueprint('api', __name__)

@api.route('/')
def hello_world():
    return "Hello world!"

@api.route("/json")
def index():
    return jsonify({"name": "alice", "email": "alice@outlook.com"})
