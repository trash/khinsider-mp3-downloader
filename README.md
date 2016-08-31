# khinsider-mp3-downloader

A script to crawl `http://downloads.khinsider.com/` for game soundtracks and download them. Downloads will be placed inside a `/downloads` directory inside the repo. Individual directories for each album will be generated automatically off the url name.

## Install
1. `$ pip install virtualenv`
2. `$ virtualenv venv`
3. `$ source venv/bin/activate`
4. `$ pip install -r requirements.txt`

## How To Use

### Input A URL Via CLI

Simply run `$ python downloader.py` from inside the repo and enter a link like 'http://downloads.khinsider.com/game-soundtracks/album/disgaea-3-raspberyl' (including the quotes) when prompted in the command line and hit enter.

### `inputs.txt`

Update the `inputs.txt` in the repo with a list of links, one link per line, and then run the script `$ python downloader.py`.
The repo includes a properly formatted `inputs.txt` for reference.

