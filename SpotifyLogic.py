
import spotify
from time import sleep
import time
import threading



class SpotifyFunctions(object):
	"""All functions the spotify client on web app must perform"""

	def __init__ (self):
		
		self.session = spotify.Session()
		self.validLogin = False
		self.name = ''
		self.searchResults = False
		self.logged_in_event = threading.Event() #USeful fr login CHeck
		self.TopArtists = []
		self.audio = spotify.AlsaSink(self.session)
		self.loop = spotify.EventLoop(self.session)
		self.loop.start()
		self.end_of_track = threading.Event()

	def connection_state_listener(self,session):
		"""login helper function"""
		if self.session.connection.state is spotify.ConnectionState.LOGGED_IN:
			self.logged_in_event.set()

	def on_end_of_track(self):
		self.end_of_track.set()

	def login(self,username,password):

		"""LOgin with 3 second time out, if state is not changed to login for whatever reason
		gives unsuccessful mesage"""
		
		self.session.on(spotify.SessionEvent.CONNECTION_STATE_UPDATED,self.connection_state_listener)
		self.session.login(username,password)
		
		startTime = time.time()
		while not self.logged_in_event.wait(0.1):
			self.session.process_events()
			currentTime = time.time()
			if currentTime - startTime > 3:
				print "LOGIN UNSUCCESFUL"
				break
		self.validLogin =True
		print "LOGIN SUCCESFUL"		

	def search(self,searchTerm):
		""" search for a string, presently edits the attribute TopArtists to 
		be the top three artists returns in the search"""
		
		self.TopArtists = []
		search = self.session.search(searchTerm)
		search.load()
		print search.artist_total
		print search.tracks[0]
		print search.artists[0].load().name
		self.TopArtists = [str(a.load().name) for a in search.artists[:3]]

	def play(self,track):
		self.session.on(spotify.SessionEvent.END_OF_TRACK, self.on_end_of_track)
		track = self.session.get_track('spotify:track:3tpdc8zHIOXy8rYhuI9car')
		track.load()
		self.session.player.load(track)
		self.session.player.play()
		try:
			while not self.end_of_track.wait(0.1):
				pass
		except KeyboardInterrupt:
			pass

		

		

		
if __name__ == '__main__':
	
	spot = SpotifyFunctions()
	spot.login('cwallac','38jgf5//')
	print spot.validLogin
	spot.search('watsky')
	print spot.TopArtists
	spot.play("BUL")

	
	

