from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

file_path = 'operadoras_ativas.csv'

try:
    df = pd.read_csv(file_path, delimiter=';', encoding='latin1')
    df = df.fillna('')
    df['Nome_Fantasia'] = df['Nome_Fantasia'].str.replace(r'\s+', ' ', regex=True)
    df['Nome_Fantasia'] = df['Nome_Fantasia'].str.strip()
except FileNotFoundError:
    print(f'Arquivo não encontrado: {file_path}')
    exit()

@app.route('/buscar', methods=['GET'])
def buscar_operadora():
    termo = request.args.get('q', '').lower().strip()
    if not termo:
        return jsonify({'erro': 'Parâmetro "q" é obrigatório'}), 400

    if 'Nome_Fantasia' not in df.columns:
        return jsonify({'erro': 'Coluna "Nome_Fantasia" não encontrada no arquivo CSV'}), 400

    resultados = df[df['Nome_Fantasia'].str.contains(termo, case=False, na=False, regex=True)]
    top_resultados = resultados.head(10).to_dict(orient='records')

    return jsonify(top_resultados)

if __name__ == '__main__':
    app.run(debug=True)