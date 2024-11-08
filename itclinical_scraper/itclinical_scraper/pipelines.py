import csv


class CsvExportPipeline:
    def open_spider(self, spider):
        # Abre o arquivo CSV quando o spider começa
        self.file = open('features.csv', mode='w',
                         newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)

        # Escreve o cabeçalho do CSV
        self.writer.writerow(['title', 'features'])

    def close_spider(self, spider):
        # Fecha o arquivo quando o spider termina
        self.file.close()

    def process_item(self, item, spider):
        # Escreve cada item (título e features) no arquivo CSV
        self.writer.writerow([item['title'], '; '.join(item['features'])])
        return item
