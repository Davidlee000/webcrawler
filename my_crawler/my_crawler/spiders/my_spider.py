import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["python.org"]
    start_urls = ["https://www.python.org"]

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