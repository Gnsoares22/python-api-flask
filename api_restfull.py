from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

clientes = [{
    'id': 0,
    'nome': 'Renato Latrel',
    'idade': 23,
    'Endereco': 'Perdizes - SP',
}]

'''  
   Veja só como é fácil criar API REST com Flask Python
   Prático, lindo e simples !!! 
   
   Obs: Neste método com a lib flask_restful não utilizaremos o jsonify como retorno das classes
'''

class clientesAdd(Resource):
    def get(self):
        return clientes
    def post(self):
        clientes.append(json.loads(request.data))
        return {'status':'200','mensagem':'Cliente registrado com sucesso !!! '}

class clientesUpdate(Resource):
    def get(self,id):
        response = clientes[id]
        return response
    def put(self,id):
        dados = json.loads(request.data)
        clientes[id] = dados
        return clientes[id]

class clientesDelete(Resource):
    def delete(self,id):
        clientes.pop(id)
        return {'status': '200', 'mensagem': 'Cliente deletado com sucesso !!! '}


# Urls do caminho com suas respectivas classes
api.add_resource(clientesAdd,'/clientes/')
api.add_resource(clientesUpdate,'/clientes/<int:id>/')
api.add_resource(clientesDelete,'/clientes/delete/<int:id>/')


if __name__ == '__main__':
    app.run(debug= True)