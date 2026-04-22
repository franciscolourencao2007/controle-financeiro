# 💳 Controle Financeiro

Sistema desktop de controle financeiro pessoal desenvolvido em Python com interface gráfica moderna.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-UI-green?style=flat)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=flat&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=flat)

---

## 🖥️ Demonstração

> Interface dark mode com cards de resumo financeiro, histórico de transações e filtros.

---

## ✅ Funcionalidades

- 📥 Registrar entradas e saídas
- ✏️ Editar transações existentes
- 🗑️ Excluir transações com confirmação
- 💰 Cálculo automático de saldo em tempo real
- 📊 Cards de resumo — Saldo, Entradas e Saídas
- 🔍 Filtro por período e tipo de transação
- 🧹 Limpar histórico completo
- 💾 Armazenamento local em banco de dados SQLite
- 🎬 Tela de splash animada ao iniciar

---

## 🧱 Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| Python 3 | Linguagem principal |
| CustomTkinter | Interface gráfica moderna com tema dark |
| Tkinter / ttk | Componente Treeview para tabela |
| SQLite3 | Banco de dados local |
| venv | Ambiente virtual isolado |

---

## 📁 Estrutura do Projeto

    Controle_financeiro/
    ├── main.py              ← ponto de entrada
    ├── requirements.txt     ← dependências
    ├── .gitignore
    ├── database/
    │   └── db.py            ← conexão com SQLite
    ├── models/
    │   └── transacao.py     ← CRUD e regras de negócio
    └── ui/
        ├── main_window.py   ← interface gráfica principal
        └── splash_screen.py ← tela de carregamento

---

## 🚀 Como Executar

**1. Clone o repositório**

    git clone https://github.com/franciscolourencao2007/controle-financeiro.git
    cd controle-financeiro

**2. Crie e ative o ambiente virtual**

    python -m venv venv
    venv\Scripts\activate

**3. Instale as dependências**

    pip install -r requirements.txt

**4. Execute o sistema**

    python main.py

---

## 🗄️ Banco de Dados

Tabela `transacoes`:

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Chave primária auto incremento |
| descricao | TEXT | Descrição da transação |
| valor | REAL | Valor monetário |
| tipo | TEXT | "Entrada" ou "Saída" |
| data | TEXT | Data no formato dd/mm/aaaa |

---

## 👨‍💻 Autor

Feito por **Francisco Lourençao**  
[![GitHub](https://img.shields.io/badge/GitHub-franciscolourencao2007-black?style=flat&logo=github)](https://github.com/franciscolourencao2007)