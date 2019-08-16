import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as requirements:
    dependencies = requirements.readlines()

setuptools.setup(
    name="LOLComicGrabber",
    version="0.0.1",
    author="Shahriyar Shawon",
    author_email="ShahriyarShawon321@gmail.com",
    description="Download League of Legends comics for offline use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShahriyarShawon/LOLComicGrabber",
    packages=["LOLComicGrabber"],
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
