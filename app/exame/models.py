from app.extensions import db 



class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer, primary_key=True)
    consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable = True)
    data = db.Column(db.Date, nullable = False)
    exam_type = db.Column(db.String(30), nullable = False)
    resultado = db.Column(db.String(300))
    medico = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable= False)
    paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)