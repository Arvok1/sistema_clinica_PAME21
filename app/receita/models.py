from ..extensions import db 
from ..association import remedios_receitas



class Receita(db.Model):
    __tablename__ = 'receita'
    id = db.Column(db.Integer, primary_key=True)
    consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'))
    remedios =  db.relationship("Remedio", secondary=remedios_receitas)
    descricao = db.Column(db.String(200))
    # As duas linhas abaixo poderiam ser usadas em um caso que toda receita precisa ser colocada no sistema 
    # junto à uma Consulta, o que não é realidade aqui, visto que Receitas podem ser incluídas vindo fora
    #medico = db.Column(db.Integer, db.ForeignKey('consulta.medico_id'))
    #paciente = db.Column(db.Integer, db.ForeignKey('consulta.paciente_id'))
    medico = db.Column(db.Integer, db.ForeignKey('medico.id'))
    paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'))