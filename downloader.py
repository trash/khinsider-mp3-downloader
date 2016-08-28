import os
from urlparse import urlparse
import urllib2, json
from bs4 import BeautifulSoup

print 'Please input link in quotes to album on khinsider.'
print 'Example input (including quotes): \'http://downloads.khinsider.com/game-soundtracks/album/disgaea-4-a-promise-unforgotten-soundtrack\''
url = input('Url: ')

# For testing
# url = 'http://downloads.khinsider.com/game-soundtracks/album/disgaea-4-a-promise-unforgotten-soundtrack'

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

# Acquire links
links = []
for anchor in anchors:
	href = anchor.get('href')
	if 'mp3' in href:
		links.append(href)

print '[info] links acquired'

downloaded_mp3s = {}

# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
# Iterate through links, grab the mp3s, and download them
for link in links:
	link_soup = BeautifulSoup(urllib2.urlopen(link))
	audio = link_soup.find('audio')
	mp3_url = audio.get('src')
	if mp3_url not in downloaded_mp3s:
		downloaded_mp3s[mp3_url] = True
		parts = mp3_url.split('/')
		file_name = parts[len(parts) - 1]

		mp3file = urllib2.urlopen(mp3_url)

		# get file size
		meta = mp3file.info()
		file_size = float(meta.getheaders("Content-Length")[0]) / 1000000

		file_on_disk_path = dir_name + '/' + file_name
		# check if file already exists
		file_already_downloaded = False
		if os.path.exists(file_on_disk_path):
			stat = os.stat(file_on_disk_path)
			file_already_downloaded = round(float(stat.st_size) / 1000000, 2) == round(file_size, 2)

		# It exists but isn't already the same size
		if not file_already_downloaded:
			print '[downloading] ' + file_name + ' [%.2f' % file_size + 'MB]'

			with open(file_on_disk_path,'wb') as output:
				output.write(mp3file.read())
				print '[done] "' + file_name + '"'
		else:
			print '[skipping] "' + file_name + '"" already downloaded.'