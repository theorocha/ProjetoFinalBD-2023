## Venv

Para utilizar esse projeto é necessário a utilização de um ambiente virtual.
No diretório principal, use os seguintes comandos para criar e ativar o venv:

```
$ virtualenv venv
$ . .venv\Scripts\activate
```

Para sair do venv:

`deactivate`

## Iniciando o projeto

Já dentro do .venv, utilize o seguinte comandos para baixar as dependências do projeto:

`pip install -r requirements.txt`

## Rodando o projeto

Para rodar o projeto basta utilizar:
`  flask --app run run --debug
 `

## Freezer requirements

Para colocar as dependencias dentro do arquivo requirements:
`  pip freeze > requirements.txt
 `
