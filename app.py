''' 
This contains the Flask app for our collaborative Spotify web app

authors: Sawyer Vaughan and Chris Wallace 
'''

from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def start():
	return render_template('start.html')

@app.route('/<url>')
def playlist(url):
	return render_template('playlist.html')

if __name__=="__main__":
	app.run()