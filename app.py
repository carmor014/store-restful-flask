from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

from db import db    

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Uso de sqlalchemy
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth

@app.before_first_request
def create_tables():
    db.init_app(app)
    db.create_all()

#items = [] # se borra porque ya no vamos a usar la memoria sino la base de datos

# la class item y class itemlist se pasaron para un nuevo script llamado item.py

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__=='__main__':    
    app.run(port=5000, debug = True)