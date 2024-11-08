# IT Affairs Scraper

This is a web scraping project using **Scrapy** to collect data from the IT Clinical website. 

## Features
Scrapes product titles and their features
Exports the data to a CSV file

# How It Works
Crawling: The spider starts by visiting the main page at https://itclinical.com/it.php and extracts all the product section links.

Data Extraction: For each product link, it navigates to the respective page and scrapes:

Title: Extracted from the "h2" tag within the page-title div.
Features: Extracted from the first list of checklist items on the page.
Data Export: The extracted data (title and features) is saved to a CSV file (features.csv) using the pipeline defined in pipeline.py.

## Requirements

Before running the scraper, make sure you have the necessary libraries installed. You can install them using the `requirements.txt` file.

## Usage
To run the Scrapy spider:

Navigate to the project directory where it_affairs.py is located:
cd itclinical_scraper

Run the spider using the Scrapy crawl command:
scrapy crawl it_affairs

The scraped data (title and features) will be printed to the console and saved into a CSV file named features.csv.

