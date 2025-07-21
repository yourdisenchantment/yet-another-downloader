# setup.py

import setuptools

setuptools.setup(
    name="image-downloader",
    version="0.1.0",
    author="Pavel",
    author_email="p.idisenchantment@gamil.com",
    description="Утилита для скачивания изображений из интернета",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourdisenchantment/image-downloader",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=open("requirements.txt").read().splitlines(),
    include_package_data=True,
)
