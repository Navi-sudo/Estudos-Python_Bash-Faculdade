from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) #F MAISCULO > TRAZ O NOME DA APLICAÇÃO
api = Api(app) #NOVA API A PARTIR DO FLASK

class main(Resource): #CRIA CLASSE PRINCIPAL > USA VERBOS HTTP COM DEF
    def get(self): #FUNÇÃO ESPECIFICA DO VERBO GET | DADOS CONTIDOS (SELF)
        msg = 'Ola mundo'
        return msg
    def post(self):
        msg = 'Ola mundo'
        return msg

class aluno(Resource):
    def get(self, nome):
        msg = 'Ola' + ' ' + nome
        return msg
    
class uisinho(Resource):
    def get(self):
        msg = 'Ola uisinho'
        return msg
            
api.add_resource(main, '/' ) #ADICIONA ROTA - CLASSE | ROTA
api.add_resource(uisinho, '/GMT') #OUTRA ROTA
api.add_resource(aluno, '/aluno/<nome>' ) #ROTA COM ADIÇÃO DE VARIAVEL 

if __name__ == '__main__':
    app.run()