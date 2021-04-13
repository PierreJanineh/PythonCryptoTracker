# PythonCryptoTracker
 
## Implementation:
* ### Get a [free developer API access](https://min-api.cryptocompare.com/) from [CryptoCompare.com](http://cryptocompae.com/) for non-commercial purposes, including historic data.
* ### Packaging:
    * Install PyInstaller with `pip3 install pyinstaller` then run `pyinstaller crypto.py` after going into your project's directory.
    * Create a `.spec` file.
  
## Icons:
We need to use `makeicns.sh` file and `chmod +x makeicns.sh` to generate an `.icns` bundle for MacOS from a single PNG: `./makeicns.sh bitcoin-icon.png`.

And for Windows we can generate an `.ico` file by loading a PNG into Gimp and resize down to 3 separate layers (64,32,16). Unlike MacOS we can provide a single square image, and it will automatically be resized, just ensure it's saved as `.ico`.

## .spec File:
For customizing your app you'll need to change `name` and resources file-paths to match yours.

> __This project is an educational example from [LearnPyQT.com](https://www.learnpyqt.com/examples/bitcoin-exchange-tracker/).__

## Setup for development:
* Install Python 3.7+ on your computer
* python -m venv _venv
* source _venv/bin/activate
* pip install -r requirements.txt
* python crypto.py

## First-time only:
* python -m venv _venv
* pip install [all the necessary libraries]
* pip freeze > requirements.txt