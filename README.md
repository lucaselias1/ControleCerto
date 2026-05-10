```markdown
# 💰 ControleCerto - Gestão de Finanças Pessoais

O **ControleCerto** é uma aplicação web completa desenvolvida para ajudar usuários a organizarem suas finanças de forma simples, visual e segura. A aplicação permite o cadastro de receitas e despesas, oferecendo um dashboard interativo com gráficos de desempenho financeiro.

## 🚀 Funcionalidades

- **Autenticação Segura**: Sistema de login e registro de usuários.
- **Gestão de Transações**: Cadastro, edição e exclusão de entradas e saídas.
- **Dashboard Interativo**: Gráficos dinâmicos utilizando Chart.js para visualização de gastos.
- **Persistência de Dados**: Integração com banco de dados PostgreSQL em ambiente de produção.
- **Interface Responsiva**: Adaptado para acesso via desktop ou dispositivos móveis.

## 🛠️ Tecnologias Utilizadas

- **Backend**: [Python](https://www.python.org/) & [Django 6.0](https://www.djangoproject.com/)
- **Frontend**: HTML5, CSS3 (Bootstrap), JavaScript & [Chart.js](https://www.chartjs.org/)
- **Banco de Dados**: PostgreSQL (Produção) / SQLite (Desenvolvimento)
- **Deploy**: [Render](https://render.com/)
- **Segurança**: Variáveis de ambiente com `python-decouple`.

## 📦 Como rodar o projeto localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/lucaselias1/ControleCerto.git](https://github.com/lucaselias1/ControleCerto.git)
   cd ControleCerto

2.  Crie e ative um ambiente virtual:
    Bash

    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No Linux/Mac:
    source venv/bin/activate

3.  Instale as dependências:
    Bash

    pip install -r requirements.txt

4.  Configure as variáveis de ambiente:
    Crie um arquivo .env na raiz do projeto e adicione:
    Code snippet

    SECRET_KEY=sua_chave_secreta
    DEBUG=True

5.  Rode as migrações e inicie o servidor:
    Bash

    python manage.py migrate
    python manage.py runserver

    Acesse: http://127.0.0.1:8000

🔗 Link do Projeto Online

Você pode conferir a aplicação rodando em: controlecerto.onrender.com

Desenvolvido por Lucas Elias