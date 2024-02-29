import os
from pymongo import MongoClient
from dotenv import load_dotenv
from scraper import Scraper
from mongo_loader import MongoLoader

load_dotenv()

client = MongoClient(os.environ['CONNECTION_STRING'])
scraper = Scraper(os.environ['URL'])
loader = MongoLoader(client)

if __name__ == '__main__':

    listings = scraper.get_all_listings(logs=True)
    loader.insert_all_listings(listings, db_name='stanovi_scraper', collection_name='listings', logs=True)

