import bottle
import logging

from bottle_sqlite import SQLitePlugin
from bottle import install

from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(filename='access.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
install(SQLitePlugin(dbfile="db.sqlite3"))


HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
API_PORT = os.getenv("API_PORT")

DEBUG = True if os.getenv("DEBUG") else False


bottle.TEMPLATE_PATH += [
    "./views/users/",
    "./views/orders/",
    "./views/categories/",
    "./views/products/",
]


MODELS = {
    "users": "Users",
    "products": "Products", 
    "categories": "Categories",
    "orders": "Orders",
}
