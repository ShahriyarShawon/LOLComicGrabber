from ..LOLComicGrabber.ComicGrabber import LOLComicGrabber

comicgrabber = LOLComicGrabber()

for series, json_content in comicgrabber.get_series().items():
    print(series)
