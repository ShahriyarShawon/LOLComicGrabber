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