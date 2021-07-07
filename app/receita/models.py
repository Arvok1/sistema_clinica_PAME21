from app.extensions import db 
from app.association import remedios_receitas


class Receita(db.Model):
    __tablename__ = 'receita'
    consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'))
    remedios =  db.relationship("Remedio", secondary=remedios_receitas)
    descricao = db.Column(db.String(200))
    medico = db.Column(db.Integer, db.ForeignKey('consulta.medico_id'))
    paciente = db.Column(db.Integer, db.ForeignKey('consulta.paciente_id'))