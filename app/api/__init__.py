from flask import Blueprint

web = Blueprint('api',__name__)

from app.api import register
from app.api import book
from app.api import user
from app.api import gift
from app.api import login
from app.api import admin
from app.api import wishes
from app.api import resetPassword
