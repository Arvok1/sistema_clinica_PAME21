'''
from app.extensions import db 



class Dia(db.Model):
    __tablename__ = 'dia'
    id = db.Column(db.Integer, primary_key=True)
    #calendario
    data = db.Column(db.Date)
    horario = db.
    #medico
    consultas = db.relationship("Consulta") 

class Calendario(db.Model):
    __tablename__ = 'calendario'
    id = db.Column(db.Integer, primary_key=True)
    #dias
    #medico
'''