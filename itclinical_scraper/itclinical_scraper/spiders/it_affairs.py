import scrapy


class ItAffairsSpider(scrapy.Spider):
    name = "it_affairs"
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        # Select all links in the "IT Affairs" section
        portfolio_links = response.xpath(
            '//ul[@class="menu"]/li[2]/ul/li/a')

        # Reverse order of the links
        portfolio_links.reverse()

        # Navigate to each product link
        for link in portfolio_links:
            # Extract title and URL
            title = link.xpath('text()').get().strip()
            url = link.xpath('@href').get()

            # Follow link to navigate
            yield response.follow(url, self.parse_section, meta={'link_title': title})

    def parse_section(self, response):
        # Get the title passed from the previous request
        link_title = response.meta['link_title']

        # Extract title from the page
        product_title = response.xpath(
            '//div[contains(@class, "sixteen floated page-title")]//h2/text()').get()

        # If the title from the page is found, use it; otherwise, use the title passed from the previous request
        title = product_title.strip() if product_title else link_title

        # Collect the list of features
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
