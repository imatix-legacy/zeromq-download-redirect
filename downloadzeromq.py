#! /usr/bin/env python
#
# download.zeromq.org simulator (Flask/WSGI application)
#
# If the URL matches a known ZeroMQ download file, send a permanent (302)
# redirect to the destination location.
#
# Otherwise for the root directory output a static result.
#
# This implementation is a quick kludge to enable using the Gandi Python/WSGI
# service instead of a more expensive IIAS VM.
#
# Written by Ewen McNeill <ewen@naos.co.nz>, 2016-06-15
#---------------------------------------------------------------------------

from flask import Flask
from flask import render_template

import csv

#---------------------------------------------------------------------------
# Configuration

REDIRECT_DATA = 'csv/zeromq-redirect.csv'
DEFAULT_PAGE  = 'zeromq-download.html'

#---------------------------------------------------------------------------
# Pre-load redirect information

REDIRECTS = {}

with open(REDIRECT_DATA, "r") as data:
    input = csv.DictReader(data)
    for row in input:
        REDIRECTS[row['filename']] = row['url']

#---------------------------------------------------------------------------
# Trivial application

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(DEFAULT_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
