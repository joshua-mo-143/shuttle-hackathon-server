#!/usr/bin/env python3

import json
from flask import Flask

from api import api
from pages import simple_page

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(simple_page)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
