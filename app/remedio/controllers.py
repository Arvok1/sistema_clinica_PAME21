from flask import Blueprint
from ..extensions import db
from .models import Remedio

remedio_api = Blueprint("remedio_api",__name__)