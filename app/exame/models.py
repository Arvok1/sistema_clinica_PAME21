from ..extensions import db 



class Exame(db.Model):
    __tablename__ = 'exame'
    id = db.Column(db.Integer, primary_key=True)
    #pode haver a informação da consulta mas ela não é necessária: O exame pode vir de fora e ser colocado no sistema
    consulta = db.Column(db.Integer, db.ForeignKey('consulta.id'), nullable = True)
    #data não podendo ser nulo evita que exames antigos sejam tratados como exames novos e vice-versa
    data = db.Column(db.Date, nullable = False)
    horario = db.Column(db.Time(timezone=True))
    #exam_type sempre necessário facilita a organização e impede que, por esquecerem de colocar tal informação
    #seja preciso procurar por vários exames para achar o correto
    exam_type = db.Column(db.String(30), nullable = False)
    resultado = db.Column(db.String(300))
    #as duas colunas abaixa possuem nullable=False para que sempre haja a informação 
    #de para quem foi passado e por quem, caso seja necessário entrar em contato por qualquer motivo
    medico = db.Column(db.Integer, db.ForeignKey('medico.id'), nullable= False) 
    paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)