import os
import threading
import urllib.parse as urlparse
import urllib.request as urllib2, json
from bs4 import BeautifulSoup

BASE_URL = 'https://downloads.khinsider.com'

def validate_url (url):
	if '//downloads.khinsider.com/game-soundtracks/album/' not in url:
		return False
	return True

def fetch_from_url (url):
	valid = validate_url(url)
	if not valid:
		print('[error] Invalid url: ' + url)
		return
	print('[info] Url found: ' + url)

	base_dir = 'downloads'
	url_parts = url.split('/')
	dir_name = base_dir + '/' + url_parts[len(url_parts) - 1]

	# Create directories
	if not os.path.exists(base_dir):
		print('[info] creating directory: ' + base_dir)
		os.makedirs(base_dir)
	if not os.path.exists(dir_name):
		print ('[info] creating directory: ' + dir_name)
		os.makedirs(dir_name)

	print('[info] crawling for links...')

	soup = BeautifulSoup(urllib2.urlopen(url))

	song_list = soup.find(id="songlist")
	anchors = song_list.find_all('a')

	# href (string) -> song name (string)
	songMap = {}

	# Acquire links
	for anchor in anchors:
		href = anchor.get('href')
		if href and 'mp3' in href:
			href = BASE_URL + href
			if href not in songMap:
				songMap[href] = anchor.string
	if not songMap:
		print('[error] No links found for the url. Double check that the url is correct and try again.')
		print('[error] url: ' + url)
		return

	print('[info] ' + str(len(songMap)) + ' links acquired')

	# Map so we don't download duplicate links on the page
	downloaded_mp3s = {}

	# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
	# Iterate through links, grab the mp3s, and download them
	for href, song_name in songMap.items():
		link_soup = BeautifulSoup(urllib2.urlopen(href))
		audio = link_soup.find('audio')
		mp3_url = audio.get('src')
		if mp3_url not in downloaded_mp3s:
			downloaded_mp3s[mp3_url] = True
			parts = mp3_url.split('/')
			file_name = song_name + '.mp3'

			file_on_disk_path = dir_name + '/' + file_name
			# check if file already exists
			file_already_downloaded = os.path.exists(file_on_disk_path)

			if not file_already_downloaded:
				print('[downloading] ' + file_name + ' [%.2f' % file_size + 'MB]')
				mp3file = urllib2.urlopen(mp3_url)

				# get file size
				meta = mp3file.info()
				file_size = float(meta.get("Content-Length")) / 1000000

				with open(file_on_disk_path,'wb') as output:
					output.write(mp3file.read())
					print('[done] "' + file_name + '"')
			else:
				print('[skipping] "' + file_name + '"" already downloaded.')

if __name__ == '__main__':
	input_file_name = 'inputs.txt'
	if os.path.exists(input_file_name):
		print('[info] Input file found. Parsing for links...')
		file = open(input_file_name, 'r')
		for line in file:
			th = threading.Thread(target=fetch_from_url, args=(line, ))
			th.start()
			threads.append(th)
	else:
		print('Please input link in quotes to album on khinsider.')
		print('Example input (including quotes): \'http://downloads.khinsider.com/game-soundtracks/album/disgaea-4-a-promise-unforgotten-soundtrack\'')
		url = input('Url: ')
		fetch_from_url(url)

# For testing
# url = 'http://downloads.khinsider.com/game-soundtracks/album/disgaea-4-a-promise-unforgotten-soundtrack'
