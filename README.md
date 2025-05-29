Este projeto consiste em uma API para realizar buscas nas operadoras de saúde, com a interface web feita em Vue.js, interagindo com o backend em Flask. A API foi configurada para buscar registros relevantes com base no nome da operadora.

Backend (Flask):
- Implementado um servidor Flask para buscar operadoras no arquivo CSV 'operadoras_ativas.csv'.
- A rota '/buscar' permite realizar buscas baseadas em um termo (por exemplo, "unimed") e retorna os registros mais relevantes.

Frontend (Vue.js):
- A interface web foi criada utilizando o Vue.js. O usuário pode digitar o nome da operadora, e o frontend faz uma requisição ao backend para obter os resultados da busca.

Testes com o Postman:
- Uma coleção do Postman foi criada para testar a rota '/buscar' da API.
- O Postman realiza uma requisição GET para buscar operadoras, como "unimed", no backend.
