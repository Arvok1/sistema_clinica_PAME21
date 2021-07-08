from flask import Blueprint
from ..extensions import db
from .models import Consulta

consulta_api = Blueprint("consulta_api",__name__)