import sqlite3

class MyDatabasePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect("scrapy_data.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                url TEXT,
                links TEXT
            )
        """)
    
    def process_item(self, item, spider):
        self.cursor.execute(
            "INSERT INTO data (title, url, links) VALUES (?, ?, ?)",
            (item["title"], item["url"], str(item["links"]))
        )
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.conn.close()