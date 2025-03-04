BOT_NAME = 'my_crawler'

SPIDER_MODULES = ['my_crawler.spiders']
NEWSPIDER_MODULE = 'my_crawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
   'my_crawler.pipelines.MyDatabasePipeline': 300,
}

# Configure delay between requests
DOWNLOAD_DELAY = 2

FEEDS = {
    'output.json': {
        'format': 'json',
        'encoding': 'utf8',
        'store_empty': False,
    },
} 