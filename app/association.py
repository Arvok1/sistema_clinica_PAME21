from .extensions import db 


remedios_receitas = db.Table('remedios_receitas',
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id')),
    db.Column('remedio_id', db.Integer, db.ForeignKey('remedio.id'))
)