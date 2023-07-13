## Sobre o projeto

Projeto é um sistema de avaliação das turmas da unb. Foi utilizado um servidor remoto  do banco de dados MySQL, e usei o python-mysql-connector para 
conexão. Toda a lógica do projeto foi desenvolvida em Flask e o front-end usado jinja para renderização
das páginas de uma maneira mais dinâmica.

## Ambientação do MySQL

Os scripts para criação do banco de dados esta em app/models, portando basta configurar seu MySQL com seu usuário(root é o padrão) e senha.
Após isso deve-se criar um schema(database) e executar o script SQL que cria as tabelas(creation_table_scripts.sql),(caso não dê certo, rode o código de cada tabela separadamente, seguindo a ordem do script)
e posteriormente inserir os dados(insertion_data.sql) seguindo a mesma lógica.

Para configuração do banco de dados, basta dentro de app/controllers/routes, no codigo que define config(linha 9), colocar 
o seu user do mysql, a senha , o host(em máquinas locais normalmente é localhost, ou manualmente pelo IP), e database(schema criado).

`config = {
    'user': 'seu_user',
    'password': 'sua_senha',
    'host': 'seu_host',
    'database': 'seu_schema'
}`

O adm do sistema deverá ter matrícula = 00.

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


