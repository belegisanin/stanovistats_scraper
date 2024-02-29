import requests
from bs4 import BeautifulSoup
from model.listing import Listing


class Scraper:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()

    def get_all_listings_from_page(self, page=1) -> list[Listing] | None:
        listings: list[Listing] = []
        full_url = f'{self.url}?p={page}'

        page_response = self.session.get(full_url)
        soup = BeautifulSoup(page_response.text, 'html.parser')

        if page_response.ok:

            listing_divs = soup.find_all('div', class_='fpogl-holder')
            for div in listing_divs:
                listing = Listing(div=div)
                listings.append(listing)

            return listings

        else:
            print(f'Unable to fetch page ({full_url}) status code: {page_response.status_code}')
            return None

    def get_all_listings(self, logs=False) -> list[Listing] | None:
        listings: list[Listing] = []
        pages = self.get_number_of_pages()

        for page in range(1, pages):
            page_listings = self.get_all_listings_from_page(page)
            listings += page_listings

            if logs:
                print(f'Total of {len(page_listings)} scraped from page {page} of {pages}')

        if logs:
            print(f'Total of {len(listings)} scraped')

        return listings

    def get_number_of_pages(self) -> int | None:
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if response.ok:
            try:
                pages = int(soup.find('ul', class_='pagination').find_all('li')[-2].a.text.strip())
                return pages
            except Exception as e:
                print(e)

        else:
            print(f'Unable to fetch page ({self.url}) status code: {response.status_code}')

        return None
