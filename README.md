# khinsider-mp3-downloader

A script to crawl `http://downloads.khinsider.com/` for game soundtracks and download them. Downloads will be placed inside a `/downloads` directory inside the repo. Individual directories for each album will be generated automatically off the url name.

## Install
The only thing you need to install is python3: https://www.python.org/downloads/

Tested and working with python 3.8.

## How To Use

### `inputs.txt`

Update the `inputs.txt` in the repo with a list of links, one link per line, and then run the script `$ python3 downloader.py`.
The repo includes a properly formatted `inputs.txt` for reference.

### Input A URL Via CLI

If you'd prefer to manually enter URLs you can delete `inputs.txt` and then simply run `$ python3 downloader.py` from inside the repo and enter a link like 'http://downloads.khinsider.com/game-soundtracks/album/disgaea-3-raspberyl' (including the quotes) when prompted in the command line and hit enter.

