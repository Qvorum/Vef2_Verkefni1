from bottle import *

@route('/')
def index():
    return "<a href='/sida/1'>Hlekkur 1</a> , <a href='/sida/2'>Hlekkur 2</a> , <a href='/sida/3'>Hlekkur 3</a>"
@route('/sida/<id>')
def index(id):
	return "Þetta er síða ", id
def index():
    return "Welkommen til jungelen!"
@error(404)
def villa(error):
	return "<h2>Þessi síða er ekki til, reyndu aftur!</h2>"
run(host='0.0.0.0', port=os.environ.get('PORT'))
#run(host='localhost', port=8080)
