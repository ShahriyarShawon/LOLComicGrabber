# replace this with from LOLComicGrabber.ComicGrabber import LOLComicGrabber in your own projects
from ..LOLComicGrabber.ComicGrabber import LOLComicGrabber

comicgrabber = LOLComicGrabber()

for series, json_content in comicgrabber.get_series().items():
    print(series)
