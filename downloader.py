import os
from urlparse import urlparse
import urllib2, json
from bs4 import BeautifulSoup

print 'Please input link in quotes to album on khinsider.'
print 'Example input (including quotes): \'http://downloads.khinsider.com/game-soundtracks/album/disgaea-4-a-promise-unforgotten-soundtrack\''
url = input('Url: ')

base_dir = 'downloads'
url_parts = url.split('/')
dir_name = base_dir + '/' + url_parts[len(url_parts) - 1]

# Create directories
if not os.path.exists(base_dir):
	print '[info] creating directory: ' + base_dir
	os.makedirs(base_dir)
if not os.path.exists(dir_name):
	print '[info] creating directory: ' + dir_name
	os.makedirs(dir_name)

print '[info] crawling for links...'

soup = BeautifulSoup(urllib2.urlopen(url))

anchors = soup.find_all('a')

links = []
for anchor in anchors:
	href = anchor.get('href')
	if 'mp3' in href:
		links.append(href)

print '[info] links acquired'

downloaded_mp3s = {}

for link in links:
	link_soup = BeautifulSoup(urllib2.urlopen(link))
	audio = link_soup.find('audio')
	mp3_url = audio.get('src')
	if mp3_url not in downloaded_mp3s:
		downloaded_mp3s[mp3_url] = True
		parts = mp3_url.split('/')
		file_name = parts[len(parts) - 1]

		print '[...] ' + file_name
		mp3file = urllib2.urlopen(mp3_url)
		with open(dir_name + '/' + file_name,'wb') as output:
			output.write(mp3file.read())
			print '[downloaded] ' + file_name