from flask import Flask, request, redirect
import random


app = Flask(__name__)

url_mappings = {}
symbols = '123abc456efg*&^789hijk'
length = 8

@app.post('/shorten')
def create_new_short_url():
    
    long_url = request.json['url']
    short_url = '/s/'
   
    for i in range(length):
        short_url += random.choice(symbols)

    if short_url not in url_mappings:
        url_mappings[short_url] = long_url
        return short_url
    else:
        return 'Error'

    

@app.get('/s/<id>')
def redirect_to_url(id):
    long_url = url_mappings.get(f'/s/{id}')

    if long_url:
        return redirect(long_url)
    else: 
        return 'Not found'

if __name__ == '__main__':
    app.run(debug=True)