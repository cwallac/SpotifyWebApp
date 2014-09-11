
import spotify

""" ADVANCED LOG IN TECHNIQUE
logged_in_event = threading.Event()

import threading
def connection_state_listener(session):
	if session.connection.state is spotify.ConnectionState.LOGGED_IN:
		logged_in_event.set()
session = spotify.Session()
session.on(spotify.SessionEvent.CONNECTION_STATE_UPDATED,connection_state_listener)
session.login('cwallac','38jgf5//')
print session.connection.state

while not logged_in_event.wait(0.1):
	session.process_events()

	"""

"""
print session.connection.state

print session.user

search = session.search('watsky')
search.load()

print search.artists[0].load().name
"""


class SpotifyFunctions(object):


	def __init__ (self):
		self.session = spotify.Session()
		self.validLogin = False
		self.name = ''

	def login(self,username,password):
		self.session.login(username,password)
		self.session.process_events()
		
		if self.session.connection.state > 0:
			self.validLogin = True
			self.name = username
			print self.SessionCallbacks.credentials_blob_updated()

		else:
			self.validLogin = False
		

		
if __name__ == '__main__':
	spot = SpotifyFunctions()
	spot.login('cwallac','38jgf5//')
	print spot.validLogin
	print spot.name

