from flask import Flask, request

app = Flask(__name__)

# Hardcoded data
next_id = 5

contacts = [
    {'id': '1', 'name': 'Shaun', 'phone': '12345678'},
    {'id': '2', 'name': 'Liz', 'phone': '00011122'}, 
    {'id': '3', 'name': 'Bob', 'phone': '1122333'},
]


# respond to all http methods
@app.route('/hello')
def hello_world():
    print('I received a request on /hello endpoint')
    return 'Hello!'

# GET method
@app.get('/contacts')
def list_contacts():
    return contacts

# route parameter
@app.get('/contacts/<id>')
def list_single(id):
    for contact in contacts:
        if contact['id'] == id:
            return contact
    return 'Contact not found'

# POST method
@app.post('/contacts')
def create_contact():
    global next_id

    print(request.json)

    new_contact = {
        'id' : f'{next_id}',
        'name': request.json['name'],
        'phone' : request.json['phone'],
    }

    contacts.append(new_contact)
    next_id += 1

    return new_contact

# PUT method
@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact
    return 'Contact not found'

# Delete method
@app.delete('/contacts/<id>')
def delete_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contacts.remove(contact)
            return contact
    return 'Contact not found'

# start the app
app.run(debug=True)