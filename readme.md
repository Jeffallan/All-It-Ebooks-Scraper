# Project Title

All IT Ebooks.com Scraper

A program that scrapes links, and other data, to your favorite tech ebooks from [allitebooks.com](http://allitebooks.com) and stores them in a MongoDB instance.

## Getting Started

Note.  One of this projects dependencies, [scrapy-mongodb](https://github.com/sebdah/scrapy-mongodb), does not support Python 3 yet.  Therefore, this project only supports Python 2

1. Clone this repository.
2. Create a new Python Virtual Environment.
3. `pip install -r requirements.txt`

## Configuration

- Create a fresh MongoDB instance either on our local machine or a free 500 MB remote instance from [MLab](https://mlab.com).

- Replace the following in settings.py with your own credentials:
```Python
MONGODB_URI = ''
MONGODB_DATABASE = ''
MONGODB_COLLECTION = ''
``` 

- Other MongoDB settings can be found here at the [scrapy-mongodb repo.](https://github.com/sebdah/scrapy-mongodb/blob/master/README.md)

## Contributing

Anyone, regardless of skill level, is encouraged to give feadback and submit pull requests.

## Acknowledgments

A special thanks to the following:

* The [Scraping Hub Team](https://github.com/scrapinghub) who maintain the [Scrapy](https://github.com/scrapy/scrapy) project;
* [Sebastian Dahlgren](https://github.com/sebdah) maintainer of [scrapy-mongodb](https://github.com/sebdah/scrapy-mongodb)
