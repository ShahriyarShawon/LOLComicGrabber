# replace this with from LOLComicGrabber.ComicGrabber import LOLComicGrabber in your own projects
from ..lolcomicgrabber.LOLComicGrabber import LOLComicGrabber

comicgrabber = LOLComicGrabber()

for series, json_content in comicgrabber.get_one_shots().items():
    print(series)
