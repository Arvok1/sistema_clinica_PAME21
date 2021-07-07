from app.extensions import db 



class Remedio(db.Model):
    __tablename__ = 'remedio'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    serve_para = db.Column(db.String(200))
    descricao = db.Column(db.String(300))
    potencia = db.Column(db.Integer)
    