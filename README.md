# Udacity-cs101-search-engine-with-Flask
A very simple search engine implemented by python which contains only simple functions.
The code Udacity course was developed from the cs101-search engine. 
The application was developed with python-flask.

Flask
=====

Flask is a lightweight `WSGI`_ web application framework. It is designed
to make getting started quick and easy, with the ability to scale up to
complex applications. It began as a simple wrapper around `Werkzeug`_
and `Jinja`_ and has become one of the most popular Python web
application frameworks.

Flask offers suggestions, but doesn't enforce any dependencies or
project layout. It is up to the developer to choose the tools and
libraries they want to use. There are many extensions provided by the
community that make adding new functionality easy.


Installing
----------

Install and update using `pip`_:


    pip install -U Flask


A Simple Example
----------------


    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, World!'


    $ env FLASK_APP=hello.py flask run
     * Serving Flask app "hello"
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Run Code 
--------

    $ cd Udacity-cs101-search-engine-with-Flask
    $ python app.py
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
