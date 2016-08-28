import os
from urlparse import urlparse
import urllib2, json
from bs4 import BeautifulSoup

base_dir = 'downloads'
dir_name = base_dir + '/' + 'disgaea 4 ost'
url = 'http://downloads.khinsider.com/game-soundtracks/album/disgaea-4-a-promise-unforgotten-soundtrack'

# Create the dir
if not os.path.exists(base_dir):
    os.makedirs(base_dir)
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

soup = BeautifulSoup(urllib2.urlopen(url))

anchors = soup.find_all('a')

links = []
for anchor in anchors:
	href = anchor.get('href')
	if 'mp3' in href:
		links.append(href)

downloaded_mp3s = {}

for link in links:
	link_soup = BeautifulSoup(urllib2.urlopen(link))
	audio = link_soup.find('audio')
	mp3_url = audio.get('src')
	if mp3_url not in downloaded_mp3s:
		downloaded_mp3s[mp3_url] = True
		parts = mp3_url.split('/')
		file_name = parts[len(parts) - 1]
		mp3file = urllib2.urlopen(mp3_url)
		with open(dir_name + '/' + file_name,'wb') as output:
			output.write(mp3file.read())
			print 'finished downloading ' + file_name
			break