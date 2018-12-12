from flask import Blueprint

web = Blueprint('api',__name__)


from app.api import book
from app.api import auth
from app.api import gift
from app.api import token