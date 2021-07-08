from flask import Blueprint
from ..extensions import db
from .models import Exame

exame_api = Blueprint("exame_api",__name__)