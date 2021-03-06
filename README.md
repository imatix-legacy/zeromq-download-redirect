# Python "WSGI" application to simulate download.zeromq.org

Designed to run as a Python/PostgreSQL "simple hosting" (PAAS)
service at Gandi:

* https://www.gandi.net/hosting/simple?language=python&db=pgsql

* https://wiki.gandi.net/en/simple/instance/python

deployed via ssh/git:

* https://wiki.gandi.net/en/simple/git

* https://wiki.gandi.net/en/simple/ssh_key

* https://wiki.gandi.net/en/gandi/ssh-keys#deployment_of_the_ssh_key_on_an_instance

# Implementation

The implementation uses [Flask](http://flask.pocoo.org/) as a simple 
WSGI handler.

For any query destination which matches a download filename, it issues
a permanent redirect to the destination URL.

For any other query it outputs the static default page.  This is actually
done with Flask's render template option, which uses 
[Jinja2](http://jinja.pocoo.org/), but since there are no Jinja2 template
elements in the static file, the file is passed through directly.

The static page (`templates/zeromq-download.html`) is generated
with the tools in the [zeromq-archived
repository](https://github.com/imatix-legacy/zeromq-archived).

Also needed are the `static` files:

*   `static/MD5SUMS`

*   `static/SHA1SUMS`

*   `static/zeromq-logo.png`

And the mapping CSV file:

*   `csv/zeromq-redirect.csv`

# License

Released under The MIT License (MIT):

Copyright (c) 2016, Naos Ltd, iMatix Corporation sprl

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject
to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
