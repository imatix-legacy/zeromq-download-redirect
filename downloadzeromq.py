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
#---------------------------------------------------------------------------
# Released under The MIT License (MIT):
#
# Copyright (c) 2016, Naos Ltd, iMatix Corporation sprl
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject
# to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#---------------------------------------------------------------------------
#
# Written by Ewen McNeill <ewen@naos.co.nz>, 2016-06-15
#---------------------------------------------------------------------------

from flask import Flask
from flask import abort, redirect, render_template

import csv

#---------------------------------------------------------------------------
# Configuration

REDIRECT_DATA = 'csv/zeromq-redirect.csv'
REDIRECT_TYPE = 301         # 301 == Permanent; 302 == Temporary
DEFAULT_PAGE  = 'zeromq-download.html'
NOT_FOUND     = 404

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

# Default page
@app.route("/")
def default():
    return render_template(DEFAULT_PAGE)

# Specific URL
@app.route("/<filename>")
def download(filename):
    if (filename in REDIRECTS):
        return redirect(REDIRECTS[filename], code=REDIRECT_TYPE)
    else:
        abort(NOT_FOUND)

if __name__ == "__main__":
    #app.run(debug=True)         # For testing only
    app.run()
