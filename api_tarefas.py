from flask import Flask , jsonify, request
import json

app = Flask(__name__)

#para mudar de apps no flask use o comando: set Flask_APP = nome_arquivo.py

tarefas = [
    {
        'id': 0,
        'responsavel': 'Gabriel',
        'tarefa': 'Construir api para registros de clientes',
        'status': 'Pendente'
    }
]

#Método POST e GET da nossa API
@app.route('/tarefas', methods = ['GET','POST'])
def inicio():
    if request.method == 'POST':
        dados = json.loads(request.data)
        tarefas.append(dados)
        return jsonify({'status':'200'})
    elif request.method == 'GET':
        return jsonify(tarefas)

@app.route('/tarefas/<int:id>/', methods = ['DELETE','GET','PUT'])
def deletar_tarefa(id):
    if request.method == 'DELETE':
        tarefas.pop(id)
        return jsonify({'status':'200','mensagem':'Tarefa deletada'})
    if request.method == 'GET':
        tarefa = tarefas[id]
        return jsonify(tarefa)
    if request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id]['status'] = dados['status']
        return jsonify(dados)

if __name__ == '__main__':
    app.run() #debug = true
