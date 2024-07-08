# Homesteads Spider

This repository contains a Scrapy spider for scraping homestead data from the Alberta Homesteads website.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

The `HomesteadsSpider` scrapes homestead data from the [Alberta Homestead Index](https://www.abgenealogy.ca/alberta-homestead-index). The spider navigates through the paginated website, extracting data fields such as surname, name, section, township, range, meridian, place name, reference, film, and file numbers.

The Alberta Homestead Index was compiled by volunteers from the [Alberta Genealogical Society (AGS)](https://www.abgenealogy.ca) transcribing the applications for land patents, including all surnames. The index includes data from the following collections:
 - Alberta Land Patents, 1885‒1897
 - Alberta Homestead Records, 1870‒1930
 - Alberta Homestead Records, post-1930

The homestead file index is an ‘all-name’ index, containing not only the name of the person who ultimately may have obtained patent on the land, but also those who may have previously applied for a homestead on that land and anyone else who appear in the file because they had some kind of interest in the land.

## Usage

1. Navigate to the project directory (if not already there):

    ```bash
    cd homesteads
    ```

2. Run the spider:

    ```bash
    scrapy crawl -o file:csv homesteads
    ```

   The scraped data will be saved according to the settings in your `items.py` and Scrapy settings. In this example, the data are exported to a file named `file.csv`.

## Project Structure

.  
├── LICENSE  
├── README.md  
├── directory-structure.md  
├── homesteads  
│   ├── __init__.py  
│   ├── __pycache__  
│   │   ├── __init__.cpython-312.pyc  
│   │   ├── items.cpython-312.pyc  
│   │   ├── middlewares.cpython-312.pyc  
│   │   ├── pipelines.cpython-312.pyc  
│   │   └── settings.cpython-312.pyc  
│   ├── items.py  
│   ├── middlewares.py  
│   ├── pipelines.py  
│   ├── settings.py  
│   └── spiders  
│       ├── __init__.py  
│       ├── __pycache__  
│       │   ├── __init__.cpython-312.pyc  
│       │   └── homesteads_spider.cpython-312.pyc  
│       └── homesteads_spider.py  
├── reference.html  
└── scrapy.cfg  

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
