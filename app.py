''' 
This contains the Flask app for our collaborative Spotify web app

authors: Sawyer Vaughan and Chris Wallace 
'''

from flask import Flask
from flask import render_template, redirect, request
from SpotifyLogic import spotifyFunctions

spotifyClasses = []

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def redirect():
	return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def start():
	return render_template('login.html')

@app.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
	x = request.form['user']
	y = request.form['password']
	new_user = spotifyLogic.spotifyFunctions()
	new_user.login(x,y)
	print new_user.validLogin
	return 'hi'

@app.route('/url_not_found')
def urlnotfound():
	return 'Playlist not found'

@app.route('/<username>', methods=['POST', 'GET'])
def playlist(username):
	global spotifyClasses
	names = []
	not_found = True
	for entry in spotifyClasses:
		if username == entry.name:
			not_found = False
			user = entry
	if not_found:
		return redirect('/url_not_found')
	return render_template('playlist.html', user=user)

if __name__=="__main__":
	app.run()