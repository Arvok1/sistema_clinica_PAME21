from flask import Blueprint
from ..extensions import db
from .models import Medico

medico_api = Blueprint("medico_api",__name__)