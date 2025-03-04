import scrapy
import sqlite3

class MySpider(scrapy.Spider):
    name = "my_spider"
    #allowed_domains = ["example.com"]  # Change to your target domain
    #start_urls = ["https://example.com"]  # Change to your target URL

    def parse(self, response):
        # Extract page title
        title = response.css("title::text").get()
        
        # Extract all links
        links = response.css("a::attr(href)").getall()
        
        yield {
            "title": title,
            "url": response.url,
            "links": links
        }

        # Follow each link and call parse method recursively
        for link in links:
            yield response.follow(link, callback=self.parse)

# Settings (add this in settings.py of your Scrapy project)
ROBOTSTXT_OBEY = True  # Obey robots.txt rules
DOWNLOAD_DELAY = 2  # Set delay to avoid getting blocked
FEEDS = {
    'output.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
    },
}

# Pipelines (add this in pipelines.py of your Scrapy project)
class MyDatabasePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("scrapy_data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (title TEXT, url TEXT)")
    
    def process_item(self, item, spider):
        self.cursor.execute("INSERT INTO data (title, url) VALUES (?, ?)", (item["title"], item["url"]))
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.conn.close()

# Enable Pipelines in settings.py
ITEM_PIPELINES = {
    'my_crawler.pipelines.MyDatabasePipeline': 300,
}

# Connect to the database
conn = sqlite3.connect('scrapy_data.db')
cursor = conn.cursor()

# Query example
cursor.execute("SELECT * FROM data")
results = cursor.fetchall()
for row in results:
    print(row)

# Close the connection
conn.close()