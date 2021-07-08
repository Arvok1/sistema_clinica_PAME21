from ..extensions import db 



class Consulta(db.Model):
    __tablename__ = 'consulta'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    horario = db.Column(db.Time(timezone=True))
    razao = db.Column(db.String(100))
    medico_id = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    comentarios = db.Column(db.String(100))
    exames_consulta = db.relationship("Exame")
    receitas = db.relationship("Receita")

    