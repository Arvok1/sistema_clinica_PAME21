from flask import Blueprint
from ..extensions import db
from .models import Paciente

paciente_api = Blueprint("paciente_api",__name__)