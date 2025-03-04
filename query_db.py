import sqlite3

def query_database():
    try:
        # Connect to the database
        conn = sqlite3.connect('scrapy_data.db')
        cursor = conn.cursor()

        # Query example
        cursor.execute("SELECT * FROM data")
        results = cursor.fetchall()
        
        # Print results
        for row in results:
            print(f"ID: {row[0]}")
            print(f"Title: {row[1]}")
            print(f"URL: {row[2]}")
            print(f"Links: {row[3]}")
            print("-" * 50)

    except sqlite3.OperationalError as e:
        print("Database error:", e)
        print("Make sure you've run the spider first to create and populate the database!")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    query_database() 