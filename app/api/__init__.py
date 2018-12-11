from flask import Blueprint

web = Blueprint('api',__name__)

from app.api import book
from app.api import auth