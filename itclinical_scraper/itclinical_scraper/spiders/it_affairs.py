import scrapy


class ItAffairsSpider(scrapy.Spider):
    name = "it_affairs"
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        # Select links in the "IT Affairs" section
        product_links = response.xpath(
            '//ul[@class="menu"]/li[2]/ul/li/a')

        # Reverse order of the links
        product_links = product_links[::-1]

        # Navigate to each product link
        for link in product_links:
            url = link.xpath('@href').get()
            # Follow the link to parse each section, using errback to handle potential errors
            yield response.follow(url, self.parse_section, errback=self.handle_request_error)

    def handle_request_error(self, failure):
        # Log the URL and details if a request fails
        self.logger.error(f'Request failed: {failure.request.url}')
        self.logger.error(repr(failure))

    def parse_section(self, response):
        # Get title directly from the software page
        title = response.xpath(
            '//div[contains(@class, "sixteen floated page-title")]//h2/text()').get()
        title = title.strip() if title else "Unknown Title"

        # Collect the list of features
        features = response.xpath(
            '(//ul[contains(@class, "check-list")])[1]//li/text()').getall()

        # If no features, log a warning and skip this item
        if not features:
            self.logger.warning(f'No features found for {title}')
            return

        # Print title and features
        print(f"\n{title}\n")
        for feature in features:
            print(f"  - {feature.strip()}")
        print("\n")

        # Yield the data for export
        yield {
            'title': title,
            'features': [feature.strip() for feature in features]
        }
