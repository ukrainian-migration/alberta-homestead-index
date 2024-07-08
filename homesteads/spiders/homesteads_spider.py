from pathlib import Path
from homesteads.items import HomesteadsItem

import scrapy

class HomesteadsSpider(scrapy.Spider):
    # Name of the spider, used to run it from the command line
    name = "homesteads"
    # List of URLs where the spider will begin to crawl
    start_urls = ["https://albertahomesteads.wefoundit.ca/?app=website&subfolder=search&task=list_buy&page=1"]

    def parse(self, response):
        # Extract data from the current page
        # Select all rows within the table inside the div with id 'asset-pdf'
        rows = response.xpath('//*[@id="asset-pdf"]/div[@class="table-responsive"]/table/tbody/tr')
        
        # Iterate over each row to extract and store data
        for row in rows:
            # Create an instance of HomesteadsItem to store the data
            item = HomesteadsItem()
            # Extract and store the surname from the second column
            item['surname'] = row.xpath('td[2]/text()').get()
            # Extract and store the first name from the third column
            item['name'] = row.xpath('td[3]/text()').get()
            # Extract and store the section number from the fourth column
            item['sec'] = row.xpath('td[4]/text()').get()
            # Extract and store the township number from the fifth column
            item['twp'] = row.xpath('td[5]/text()').get()
            # Extract and store the range number from the sixth column
            item['rge'] = row.xpath('td[6]/text()').get()
            # Extract and store the meridian number from the seventh column
            item['mer'] = row.xpath('td[7]/text()').get()
            # Extract and store the place name from the eighth column
            item['placename'] = row.xpath('td[8]/text()').get()
            # Extract and store the reference number from the ninth column
            item['ref'] = row.xpath('td[9]/text()').get()
            # Extract and store the film number from the tenth column
            item['film'] = row.xpath('td[10]/text()').get()
            # Extract and store the file number from the eleventh column
            item['file'] = row.xpath('td[11]/text()').get()
            # Yield the item, sending it to the pipeline
            yield item
        
        # Pagination handling        
        # Extract the current page number from the URL
        current_page = int(response.url.split('page=')[-1])
        # Define the total number of pages
        num_pages = 64747

        # Check if there are more pages to scrape
        if current_page < num_pages:
            # Construct the URL for the next page
            next_page = f"https://albertahomesteads.wefoundit.ca/?app=website&subfolder=search&task=list_buy&page={current_page + 1}"
            # Follow the next page link and call the parse method on the response
            yield response.follow(next_page, callback=self.parse)
