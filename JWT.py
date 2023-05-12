from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'monstro'  # chave secreta para a geração de token JWT
jwt = JWTManager(app)


# Criando uma rota de autenticação que retorna um token JWT
@app.route('/login', methods=['POST'])
def login():
    # Aqui você pode realizar a lógica de autenticação do seu sistema
    # Se a autenticação for bem-sucedida, crie e retorne um token JWT
    access_token = create_access_token(identity='username')
    return jsonify({'access_token': access_token})


# Criando uma rota protegida por autenticação JWT que retorna o JSON
@app.route('/treino', methods=['GET'])
@jwt_required()  # decora a rota com @jwt_required para exigir autenticação
def protected():
    # Aqui você pode buscar os dados da sua base de dados e transformá-los em JSON
    # Depois, retorne o JSON
    data = {
        'grupoMuscular': [
            {'id': 1, 'nome': 'Costas'},
            {'id': 2, 'nome': 'Bíceps'},
            {'id': 3, 'nome': 'Tríceps'}
        ],
        'exercicios': [
            {'id': 1, 'nome': 'Pull Down', 'grupo': 1},
            {'id': 2, 'nome': 'Rosca Martelo', 'grupo': 2},
            {'id': 3, 'nome': 'Supino', 'grupo': 3}
        ],
        'exercicioTreino': [
            {'id': 1, 'exercicio': 1, 'repeticao': 10, 'peso': 20, 'series': 3},
            {'id': 2, 'exercicio': 2, 'repeticao': 12, 'peso': 15, 'series': 4},
            {'id': 3, 'exercicio': 3, 'repeticao': 8, 'peso': 30, 'series': 5}
        ],
        'treinoDiario': [
            {'id': 1, 'dia': '2023-05-12', 'executado': 1, 'exercicio': 1},
            {'id': 2, 'dia': '2023-05-12', 'executado': 1, 'exercicio': 2},
            {'id': 3, 'dia': '2023-05-12', 'executado': 0, 'exercicio': 3}
        ],
        'treino': [
            {'treinoDiario': 1, 'dataInicio': '2023-05-10', 'dataFim': '2023-05-15', 'aluno': 1},
            {'treinoDiario': 2, 'dataInicio': '2023-05-10', 'dataFim': '2023-05-15', 'aluno': 1},
            {'treinoDiario': 3, 'dataInicio': '2023-05-10', 'dataFim': '2023-05-15', 'aluno': 2}
        ]
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run()

