import scrapy


class ItAffairsSpider(scrapy.Spider):
    name = "it_affairs"
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        # Select all links in the software section
        portfolio_links = response.xpath(
            '//a[contains(@class, "portfolio-item")]/@href').getall()

        # Reverse the order of the links
        portfolio_links.reverse()

        # Navigate to each product link
        for link in portfolio_links:
            yield response.follow(link, self.parse_section)

    def parse_section(self, response):
        # Collect the page title
        title = response.xpath(
            '//div[contains(@class, "sixteen") and contains(@class, "floated") and contains(@class, "page-title")]/h2/text()').get().strip()

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
