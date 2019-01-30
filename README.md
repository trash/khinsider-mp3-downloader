# khinsider-mp3-downloader

A script to crawl `http://downloads.khinsider.com/` for game soundtracks and download them. Downloads will be placed inside a `/downloads` directory inside the repo. Individual directories for each album will be generated automatically off the url name.

## Install
1. Install python from python.org if you haven't already. This will install `pip` so it can be nice to do either way.
2. `$ pip install virtualenv`
3. Start a new terminal instance inside the repository directory (`khinsider-mp3-downloader/`) so you can call `virtualenv`
4. `$ virtualenv venv`
5. `$ source venv/bin/activate`
6. `$ pip install -r requirements.txt`

## How To Use

### `inputs.txt`

Update the `inputs.txt` in the repo with a list of links, one link per line, and then run the script `$ python downloader.py`.
The repo includes a properly formatted `inputs.txt` for reference.

### Input A URL Via CLI

If you'd prefer to manually enter URLs you can delete `inputs.txt` and then simply run `$ python downloader.py` from inside the repo and enter a link like 'http://downloads.khinsider.com/game-soundtracks/album/disgaea-3-raspberyl' (including the quotes) when prompted in the command line and hit enter.

