# Desafio_PicPay

# Sobre o projeto [PT-BR]

O projeto Backend proposto como desafio PicPay simplificado consiste em criar  um serviço que disponibilize uma API REST que implemente funcionalidades e requisitos técnicos descritos pelo link: https://github.com/PicPay/picpay-desafio-backend/blob/master/readme.md

Nesse projeto foi utilizado Django REST framework e foram atendidos os requisitos:

Para ambos tipos de usuário, precisamos do Nome Completo, CPF, e-mail e Senha. CPF/CNPJ e e-mails devem ser únicos no sistema. Sendo assim, seu sistema deve permitir apenas um cadastro com o mesmo CPF ou endereço de e-mail.

Usuários podem enviar dinheiro (efetuar transferência) para lojistas e entre usuários.

Lojistas só recebem transferências, não enviam dinheiro para ninguém.

Validar se o usuário tem saldo antes da transferência.

A operação de transferência deve ser uma transação (ou seja, revertida em qualquer caso de inconsistência) e o dinheiro deve voltar para a carteira do usuário que envia.

Este serviço deve ser RESTFul.


# Tecnologias utilizadas
## Back end
- Python
- Django REST framework
- Banco de dados: SQLite

# Como executar o projeto

## Back end
Pré-requisitos: Django e Python

```bash
# clonar repositório
git clone https://github.com/AllanGomesCorrea/Desafio_PicPay.git

# criar o virtual environment
python3 -m venv venv

# ativar a venv (Linux,macOS)
source venv/bin/activate

# ativar a venv (Windows)
venv\Scripts\activate

# executar o comando para instalação das versões
pip install -r ./requirements.txt

# executar o projeto
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Resultado

Através do Django foi possível testar localmente e obter os resultados utlizando o endereço: http://127.0.0.1:8000/api/v1/users/

Uma collection do Postman foi adicionada aos arquivos para realização dos testes propostos.

# Autor

[![Autor](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/allan-correa-582086186/)

Allan Gomes Corrêa





