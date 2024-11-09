import scrapy


class ItAffairsSpider(scrapy.Spider):
    name = "it_affairs"
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        # Select all links in the "IT Affairs" section
        portfolio_links = response.xpath(
            '//ul[@class="menu"]/li[2]/ul/li/a')

        # Reverse the order of the links
        portfolio_links.reverse()

        # Navigate to each product link
        for link in portfolio_links:
            # Extract title and URL
            title = link.xpath('text()').get().strip()
            url = link.xpath('@href').get()

            # Follow the link to navigate to the product page
            yield response.follow(url, self.parse_section, meta={'title': title})

    def parse_section(self, response):
        # Get the title passed from the previous request
        title = response.meta['title']

        # Collect the first list of features (checklist items)
        features = response.xpath(
            '(//ul[contains(@class, "check-list")])[1]//li/text()').getall()

        # Print the title and features
        print(f"\n{title}\n")
        for feature in features:
            print(f"  - {feature.strip()}")
        print("\n")

        # Yield the data for export
        yield {
            'title': title,
            'features': [feature.strip() for feature in features]
        }
