from flask import Blueprint, request, jsonify
from flask.templating import render_template
from ..extensions import db
from .models import Paciente

paciente_api = Blueprint("paciente_api",__name__)

@paciente_api.route('/criar_paciente', methods=['GET', 'POST'])
def criar_paciente():
    if request.method == 'GET':
        return render_template("templates/criar_paciente.html")#a ideia é retornar a interface aqui
    
    elif request.method == 'POST':
        dados_paciente = request.get_json(force=True) 
        nome_paciente = dados_paciente["nome"]  
        cpf_paciente = dados_paciente["cpf"]
        email_paciente = dados_paciente["email"]
        telefone_paciente = dados_paciente["telefone"]
        idade_paciente = dados_paciente["idade"]
        genero_paciente = dados_paciente["genero"]
        if isinstance(nome_paciente, str) and isinstance(cpf_paciente, int) and (isinstance(email_paciente, str) or email_paciente is None) and isinstance(telefone_paciente, str) and (isinstance(idade_paciente, int) or idade_paciente is None) and (isinstance(genero_paciente, str) or genero_paciente is None):
            paciente_existente = Paciente.query.filter_by(cpf=cpf_paciente)
            if not paciente_existente:#se paciente não existir, executará as linhas abaixo
                novo_paciente = Paciente(nome = nome_paciente, cpf = cpf_paciente, email=email_paciente, telefone=telefone_paciente, idade = idade_paciente, genero=genero_paciente)
                #Dá para poupar memória aqui fazendo a criação do objeto de maneira direta
                #Seria feito da seguinte forma: Paciente(nome=dados_paciente["nome"])
                #Entretanto, a escolha por esse método deixa o código mais claro, na minha opinião
                db.session.add(novo_paciente)
                db.session.commit()
                paciente_criado = Paciente.query.filter_by(cpf=cpf_paciente)
                return render_template("paciente_criado.html", paciente=paciente_criado)
            else:
                return jsonify(
                    erro="O paciente já existe"
                )        
        else:
            return jsonify(
                erro="Alguma informação foi inserida errada"
            )
            #json avisando error
#Não sei exatamente como tratar o código aqui: Conheço sobre Flask mas usando o que o python dá, 
#sem usar JSON e fazendo a ligação diretamente entre front e back usando Jinja, dessa maneira, peço
#desculpas por qualquer erro aqui