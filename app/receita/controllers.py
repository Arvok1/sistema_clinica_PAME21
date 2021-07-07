from flask import Blueprint
from ..extensions import db
from .models import Receita

receita_api = Blueprint("receita_api",__name__)