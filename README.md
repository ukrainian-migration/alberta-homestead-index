# Homesteads Spider

This repository contains a Scrapy spider for scraping homestead data from the Alberta Homesteads website.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

The `HomesteadsSpider` scrapes homestead data from the Alberta Homesteads website. The spider navigates through the paginated website, extracting relevant data fields such as surname, name, section, township, range, meridian, place name, reference, film, and file numbers.

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
