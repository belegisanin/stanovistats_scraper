from bs4 import PageElement
import utils


class Listing:
    def __init__(self, id=None, title=None, city=None, price=None, area=None, furniture=None, date=None, div=None):
        if div:
            try:
                self.title = div.find('h2', itemprop='name').text.strip()
                self.id = utils.static_hash(self.title)

                price_element = div.find('span', {'itemprop': 'price'})
                self.price = float(price_element.get('content')) if price_element else None

                flat_info = div.find_all('div', class_='col-sm-6')
                flat_surface_area = flat_info[2].strong.text.strip() if flat_info and len(flat_info) > 2 else None
                self.area = int(flat_surface_area[:-2]) if flat_surface_area else None
                self.furniture = flat_info[1].strong.text.strip() if flat_info and len(flat_info) > 1 else None

                last_edit_time = div.find('time', datetime=True)
                self.date = utils.parse_date(last_edit_time.text.strip() if last_edit_time else None)

                city_element = div.find_all('a', itemprop='category', href=True)[2]
                self.city = city_element.text.strip() if city_element else None
            except Exception as e:
                print(e)
        else:
            self.id = id
            self.title = title
            self.city = city
            self.price = price
            self.area = area
            self.furniture = furniture
            self.date = date

    def to_dict(self) -> dict:
        return {'_id': self.id, 'title': self.title, 'city': self.city,
                'price': self.price, 'area': self.area, 'furniture': self.furniture, 'date': self.date}
