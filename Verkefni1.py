from bottle import *
import os

@route('/')
def index():
    return "Halló heimur nú er gaman..."

run(host='0.0.0.0', port=os.environ.get('PORT'))
