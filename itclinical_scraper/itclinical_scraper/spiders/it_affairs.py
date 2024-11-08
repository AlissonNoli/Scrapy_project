import scrapy


class ItAffairsSpider(scrapy.Spider):
    name = "it_affairs"
    start_urls = ["https://itclinical.com/it.php"]

    def parse(self, response):
        # Seleciona todos os links nas seções de software
        portfolio_links = response.css('a.portfolio-item::attr(href)').getall()

        # Navega para cada link de produto
        for link in portfolio_links:
            yield response.follow(link, self.parse_section)

    def parse_section(self, response):
        # Coleta o título da página
        title = response.css(
            'div.sixteen.floated.page-title h2::text').get().strip()

        # Coleta a lista de funcionalidades
        features = response.css('ul.check-list li::text').getall()

        # Exibe o título e as features no console
        print(f"\n{'='*40}\n{title}\n{'='*40}")
        for feature in features:
            print(f"  - {feature.strip()}")
        print("\n")

        # Envia os dados para o pipeline
        yield {
            'title': title,
            'features': [feature.strip() for feature in features]
        }
