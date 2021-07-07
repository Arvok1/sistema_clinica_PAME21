from app.extensions import db 



class Medico(db.Model):
    __tablename__ = 'medico'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(12))
    idade = db.Column(db.Integer)
    genero = db.Column(db.string(10))
    cpf = db.Column(db.Integer)
    crm = db.Column(db.Integer)
    especialidade = db.Column(db.String(20))
    localidade = db.Column(db.String(9))#pode ser interno ou externo    
    consultas = db.relationship("Consulta")
    exames_pedidos = db.relationship("Exame")