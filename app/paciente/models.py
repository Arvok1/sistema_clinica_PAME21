from ..extensions import db 


class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    nome = db.Column(db.String(20))
    cpf = db.Column(db.Integer)
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(12))
    idade = db.Column(db.Integer)
    genero = db.Column(db.String(10))
    consultas = db.relationship("Consulta")
    exames = db.relationship("Exame")
    receitas = db.relationship("Receita")