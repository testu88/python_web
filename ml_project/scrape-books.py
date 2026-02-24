import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)

# Parse / pull data out of html/xml files
soup = BeautifulSoup(response.text, 'html5lib')

# Get data in html tag and class

books = []

for item in soup.find_all('article', class_='product_pod'):
    title = item.find('h3').find('a').text
    price = item.find('p', class_='price_color').text
    star_rating = item.find('p', class_='star-rating')
    rating = star_rating.get('class')[1]
    book = {
        'title': title,
        'price': price,
        'rating':rating,
    }
    books.append(book)

print(books)