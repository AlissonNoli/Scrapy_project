import csv


class CsvExportPipeline:
    def open_spider(self, spider):
        # Open CSV file when the spider starts
        self.file = open('features.csv', mode='w',
                         newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)

        #  Write CSV headers
        self.writer.writerow(['title', 'features'])
        spider.logger.info("CSV file opened and header written.")

    def close_spider(self, spider):
        # Close the file when the spider finishes
        self.file.close()
        spider.logger.info("CSV file closed.")

    def process_item(self, item, spider):
        # Write each item (title and features) to the CSV file
        self.writer.writerow([item['title'], ';'.join(item['features'])])
        return item
