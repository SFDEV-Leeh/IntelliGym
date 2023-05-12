from crudDB import SQLiteCRUD 

bd_path = "Banco\BD\intellyGym.db"

def get_treino(id, date):
    columns = ['treino.dataInicio', 'treino.dataFim', 'treinoDiario.dia', 'treinoDiario.executado', 
            'exercicioTreino.repeticao', 'exercicioTreino.peso', 'exercicioTreino.series', 
            'exercicios.nome AS nome_exercicio', 'grupoMuscular.nome AS nome_grupoMuscular']
    where = f'aluno = {id} AND treinoDiario.dia = "{date}"'
    join = '''JOIN treinoDiario ON treino.treinoDiario = treinoDiario.id
            JOIN exercicioTreino ON treinoDiario.exercicio = exercicioTreino.id
            JOIN exercicios ON exercicioTreino.exercicio = exercicios.id
            JOIN grupoMuscular ON exercicios.grupo = grupoMuscular.id
            '''
    db = SQLiteCRUD(bd_path)
    result = db.select('treino', columns, where, join)
    
    return result

def get_user_info(id):
    columns = ['aluno.id', 'aluno.nome', 'aluno.email', 'aluno.celular', 
            'aluno.dtNascimento', 'aluno.endereco', 'exercicioTreino.series', 
            'exercicios.nome AS nome_exercicio', 'grupoMuscular.nome AS nome_grupoMuscular']

        
    db = SQLiteCRUD(bd_path)
    result = db.select('aluno')
    
    return result

