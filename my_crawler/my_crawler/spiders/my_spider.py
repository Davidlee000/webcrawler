import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"
    allowed_domains = ["python.org"]
    start_urls = ["https://www.python.org"]

    def parse(self, response):
        yield {
            "title": response.css("title::text").get(),
            "url": response.url,
            "links": response.css("a::attr(href)").getall()
        }

        # Follow links
        for link in response.css("a::attr(href)").getall():
            yield response.follow(link, callback=self.parse) 