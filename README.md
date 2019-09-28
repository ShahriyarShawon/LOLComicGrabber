# LOLComicGrabber

LOLComicGrabber is a python package aimed at making downloading the League of Legends comic books possible. I made this because I didn't want to be limited to a browser and internet connection to read one of these comics. LOLComicGrabber aims to make the League of Legends comics accessible.

# Installation
Install from pip

```bash 
pip install LOLComicGrabber
```

or install from source

```bash
git clone https://github.com/ShahriyarShawon/LOLComicGrabber.git
```
```bash
cd LOLComicGrabber
```
```bash
python setup.py install 
```


# Usage

## As CLI App

```
usage: lcg [-h] [-t TITLE] [-s SERIES] [-i ISSUE] action type

positional arguments:
  action                Determines whether you want to `list` or `download`
  type                  Describes whether your selection is a `one_shot` or a
                        `series`

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        Title of the one shot you want to download
  -s SERIES, --series SERIES
                        Name of series you want to download
  -i ISSUE, --issue ISSUE
                        If downloading series, needs which issue
```

List Series and One shots
```
lcg list one_shots
```
```
lcg list series
```



Download Issue 4 of Ashe Warmother
```
lcg download series -s Warmother -i 4
```

Download One shot

```
lcg download one_shot -t "Nami: Into the Abyss"
```

## As Python Library/Package

Download Issue 3 of Ashe Warmother
```python
from LOLComicGrabber.ComicGrabber import LOLComicGrabber

grabber = LOLComicGrabber()
grabber.download("Warmother",3)
```

List one shots
```python
from LOLComicGrabber.ComicGrabber import LOLComicGrabber

grabber = LOLComicGrabber()
for key,value in grabber.get_one_shots().items():
    print(key)
```

Download One Shot
```python
from LOLComicGrabber.ComicGrabber import LOLComicGrabber

grabber = LOLComicGrabber()
grabber.download("Nami: Into the Abyss", is_series=False)
```


# What's New?

0.0.2 - Made filename and directory names friendly for Windows