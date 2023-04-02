# Mutual API

Este é o repositório da Mutual API, aplicativo que contém 3 endpoints que realizam determinadas operações com frases e números.

## Funcionalidades
- `reverse_integer`: Inverte a ordem dos algarismo em um número inteiro.
- `average_length`: Calcula a média de letras por palavra em uma frase.
- `matched_mismatched_words`: Identifica palavras comuns e não comuns entre duas frases.

## Rodando o App

Para rodar este aplicativo, você pode seguir os seguintes passos:

1. Certifique-se de que você tem o Python instalado em sua máquina. Você pode baixar o Python em https://www.python.org/downloads/.
2. Clone o repositório do aplicativo em sua máquina local.
3. Navegue até o diretório do aplicativo clonado.
4. Instale as dependências necessárias usando o seguinte comando: `pip install -r requirements.txt`
5. Para executar o aplicativo, execute o seguinte comando: `python main.py`
6. O aplicativo estará sendo executado em http://127.0.0.1:8000/. Faça as chamadas para a api utilizando essa url.
- Para parar o aplicativo, pressione Ctrl + C no terminal.

## Como usar a API
### Reverse Integers
Para inverter um número inteiro, faça uma solicitação GET para /reverse_integer/{number}, onde {number} é o número que você deseja inverter. O número pode ser positivo, negativo ou zero. A resposta será um JSON com uma única chave "reverse integer" e o valor será o número invertido.

### Average Words Length
Para obter o comprimento médio das palavras em uma string, faça uma solicitação POST para /average_length com o corpo em JSON {"phrase": "string"}, onde "string" é a string na qual você deseja calcular o comprimento médio das palavras. A resposta será um JSON com uma única chave "average length" e o valor será o comprimento médio das palavras na string.

### Matched & Mismatched Words
Para obter as palavras correspondentes e não correspondentes entre duas frases, faça uma solicitação POST para /matched_mismatched_words com o corpo em JSON {"phrase1": "string1", "phrase2": "string2"}, onde "string1" e "string2" são as duas frases que você deseja comparar. A resposta será um JSON com duas chaves "matched words" e "mismatched words". "matched words" será uma lista de palavras que aparecem em ambas as frases, e "mismatched words" será uma lista de palavras que aparecem em apenas uma das frases.

## Docker
### Este aplicativo também pode ser executado em um contêiner Docker. Para fazer isso, siga estas etapas:

- Certifique-se de que o Docker esteja instalado em sua máquina.
- Clone o repositório usando o comando git clone.
- Crie a imagem Docker executando `docker build -t app`. dentro do diretório do aplicativo. Isso criará uma imagem chamada app.
- Execute o contêiner com o comando `docker-compose up`. Isso executará o contêiner e mapeará a porta do contêiner 80 para a porta 8000 do host.

