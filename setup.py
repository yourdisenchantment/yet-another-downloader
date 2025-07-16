# setup.py

from setuptools import find_packages, setup

setup(
    name="image-downloader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "stealth-requests",
        "fake-useragent",
    ],
    python_requires=">=3.13",
)
