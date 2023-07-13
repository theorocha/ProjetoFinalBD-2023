## Sobre o projeto

Projeto é um sistema de avaliação das turmas da unb. Foi utilizado um servidor remoto  do banco de dados MySQL, e usei o python-mysql-connector para 
conexão. Toda a lógica do projeto foi desenvolvida em Flask e o front-end usado jinja para renderização
das páginas de uma maneira mais dinâmica.

Os scripts para criação do banco de dados esta em app/models.


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


