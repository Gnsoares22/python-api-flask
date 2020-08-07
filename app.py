from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [{ 'nome':'gabriel',
                     'habilidades':['Python','.Net']},
                   {'nome':'Kethellen',
                    'habilidades': ['React.js', 'React Native']}
                   ]


@app.route('/dev/<int:id>/', methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except Exception as ex:
            response = {'status': 'erro', 'mensagem': ex}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso','mensagem':'Registro Deletado'})

#Lista todos desenvolvedores e cadastra desenvolvedor
@app.route('/dev/',methods = ['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == "__main__":
    app.run(debug = True)