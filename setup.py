import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as requirements:
    dependencies = requirements.readlines()

current_version = "0.0.3"

setuptools.setup(
    name="LOLComicGrabber",
    version=current_version,
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
    entry_points={
        "console_scripts": [
            "lcg = LOLComicGrabber.__main__:main"
        ]
    }
)
