import scrapy


class ItAffairsSpider(scrapy.Spider):
    name = "it_affairs"
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        # Select all links in the software sections
        portfolio_links = response.css('a.portfolio-item::attr(href)').getall()

        # Navigate to each product link
        for link in portfolio_links:
            yield response.follow(link, self.parse_section)

    def parse_section(self, response):
        # Collects the page title
        title = response.css(
            'div.sixteen.floated.page-title h2::text').get().strip()

        # Collect the list of features
        features = response.css('ul.check-list li::text').getall()

        # Displays the title and features on the console
        print(f"\n{'='*40}\n{title}\n{'='*40}")
        for feature in features:
            print(f"  - {feature.strip()}")
        print("\n")

        # Sends data to the pipeline
        yield {
            'title': title,
            'features': [feature.strip() for feature in features]
        }
