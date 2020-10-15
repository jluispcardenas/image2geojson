import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image2geojson",
    py_modules = ['image2geojson'],
    version="0.0.1",
    author="Jose Luis Cardenas",
    author_email="jluispcardenas@gmail.com",
    description="Convert image to GeoJSON",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jluispcardenas/image2geojson",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    license = "MIT",
    keywords = ['geojson', 'geo', 'latitude', 'longitude', 'coordinates', 'circle', 'image'],
    install_requires = ['argparse', 'opencv-python'],
    entry_points='''
	   [console_scripts]
	   image2geojson=image2geojson:main
          '''
)
