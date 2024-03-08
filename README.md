# stanovistats_scraper - Real Estate Scraper Project

**Overview**

This Python project is a small web scraper designed to collect information about apartment prices and other related details from a popular online source. The collected data is then stored in a MongoDB database for further analysis or use.

**Features**

1. **Web Scraping:** Uses web scraping techniques to extract information about apartment prices, location, and other relevant data from real estate websites.

2. **MongoDB Integration:** Stores the collected data in a MongoDB database for easier retrieval and manipulation.

3. **Adaptability:** Can be easily adapted to target different real estate websites or adjust to changes in website structure.

**Prerequisites**

- Python 3.x
- MongoDB installed and running (or hosted MongoDB Atlas)
- Required Python packages can be installed using:

  ```bash
  pip install -r requirements.txt
  ```

**Usage**

1. **Clone the repository:**

  ```bash
  git clone [https://github.com/belegisanin/stanovistats_scraper.git](https://github.com/belegisanin/stanovistats_scraper.git)
  ```

2. **Navigate to the project directory:**

  ```bash
  cd stanovistats_scraper
  ```

3. **Configuration:**

  Create a file named `.env` to add the URLs of the real estate websites you want to scrape and authentication details for MongoDB.

4. **Run the Scraper:**

  ```bash
  python main.py
  ```

  This will start the scraping process and populate the MongoDB database with the collected data.

**Configuration**

The `.env` file contains parameters such as MongoDB connection details and website URLs. Customize this file according to your preferences.

```python
# MongoDB configuration
CONNECTION_STRING = mongodb://localhost:27017/...

# URL for scraping
URL=https://...
```

**Notes**

1. Make sure your web scraping activities comply with the terms of service of the targeted websites.

2. Periodically check and update the scraper according to changes in the website structures.

3. This project is for educational purposes and should be used responsibly.

**License**

This project is licensed under the MIT License. Feel free to contribute.
