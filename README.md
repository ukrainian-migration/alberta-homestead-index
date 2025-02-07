# Homesteads Spider

This repository contains a [Scrapy](https://scrapy.org) spider for scraping homestead data from the Alberta Homestead Index website.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

The `homesteads` spider scrapes homestead data from the [Alberta Homestead Index](https://www.abgenealogy.ca/alberta-homestead-index). The spider navigates through the paginated website, extracting data fields such as surname, name, section, township, range, meridian, place name, reference, film, and file numbers.

The Alberta Homestead Index was compiled by volunteers from the [Alberta Genealogical Society (AGS)](https://www.abgenealogy.ca) transcribing the applications for land patents, including all surnames. The index includes data from the following collections:
 - Alberta Land Patents, 1885‒1897
 - Alberta Homestead Records, 1870‒1930
 - Alberta Homestead Records, post-1930

The homestead file index is an ‘all-name’ index, containing not only the name of the person who ultimately may have obtained patent on the land, but also those who may have previously applied for a homestead on that land and anyone else who appear in the file because they had some kind of interest in the land.

## Usage

Each scraper is unique to the project for which it is designed. The code in this repository is meant to be illustrative of the data collection process for the Ukrainian migration project.

Scrapy must be installed on the machine running the code. Read the [Scrapy documentation](https://docs.scrapy.org/en/latest/intro/install.html) for more information on installation. Once installed and configured, the spider runs using the following terminal command:

```console
scrapy crawl -o file:csv homesteads
```

The scraped data is saved according to the settings in `items.py` and `settings.py`. In the above example, the data are exported to a file named `file.csv`.

## Project Structure

```
.  
├── LICENSE  
├── README.md  
├── homesteads  
│   ├── __init__.py  
│   ├── items.py  
│   ├── middlewares.py  
│   ├── pipelines.py  
│   ├── settings.py  
│   └── spiders  
│       ├── __init__.py  
│       └── homesteads_spider.py  
├── reference.html  
└── scrapy.cfg  
```

- `homesteads`: The main project directory.
- `items.py`: Defines the data structures for the scraped items.
- `middlewares.py`: Contains custom middlewares (if any).
- `pipelines.py`: Contains item pipeline definitions.
- `settings.py`: Contains project settings.
- `spiders`: Directory containing spider definitions.
- `scrapy.cfg`: Scrapy configuration file.
- `README.md`: Project documentation file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
