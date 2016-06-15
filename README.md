# Python "WSGI" application to simulate download.zeromq.org

Designed to run as a Python/PostgreSQL "simple hosting" (PAAS)
service at Gandi:

https://www.gandi.net/hosting/simple?language=python&db=pgsql
https://wiki.gandi.net/en/simple/instance/python

deployed via ssh/git:

https://wiki.gandi.net/en/simple/git
https://wiki.gandi.net/en/simple/ssh_key
https://wiki.gandi.net/en/gandi/ssh-keys#deployment_of_the_ssh_key_on_an_instance

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
