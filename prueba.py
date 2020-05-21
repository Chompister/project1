from flask import Flask
app = Flask(__name__)
@app.route('/')
def hola_ubunlog():
	return 'Hola Ubunlog'