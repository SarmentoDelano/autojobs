# 🤖 AutoJobs

<p align="center">
  <img src="frontend/public/robot-icon.png" alt="AutoJobs logo" width="120"/>
</p>

Sistema inteligente para busca automática de vagas em diversos sites de emprego.

---

## 📋 Descrição

O **AutoJobs** automatiza a busca por vagas tech em múltiplas plataformas (como Gupy, Programathor, Remotar, Vagas.com e InfoJobs), organizando tudo em um painel visual intuitivo.

🔎 Basta digitar uma palavra-chave para encontrar, filtrar e salvar as oportunidades que interessam.

Ideal para quem busca praticidade, foco em tecnologia e centralização de buscas.

---

## 💻 Interface

![image](https://github.com/user-attachments/assets/cd9922e6-ec13-4132-b552-02c02142e3a7)


### 🎯 Funcionalidades:
- 🔍 Busca por palavra-chave
- 🧠 Webscraping inteligente com feedback em tempo real
- ⭐ Favoritar vagas para não perder oportunidades
- 📦 Filtros por plataforma
- 🧹 Limpeza de banco preservando favoritos

---

## 🛠️ Tecnologias

### Backend
- Python 3.11
- Django & Django REST Framework
- Selenium + Undetected ChromeDriver

### Frontend
- React.js
- TailwindCSS
- Axios
- EventSource (streaming de progresso)

### Outros
- PostgreSQL
- Figma (protótipos)

---

## 🚀 Como executar localmente

### Backend
```bash
# Navegue até a pasta backend
cd backend

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o backend
python manage.py runserver
```

### Frontend
```bash
# Em outra aba/terminal
cd frontend
npm install
npm start
```

## 📄 Licença
Projeto pessoal com fins educacionais. Código aberto sob a licença MIT.

---

## ✉️ Contato

Feito por Delano Sarmento.  
[LinkedIn](https://www.linkedin.com/in/delanosarmento/) | [GitHub](https://github.com/SarmentoDelano)
