# BugTracker — Sistema CRUD de Gestão de Bugs

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-success?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)

---

Um sistema simples e moderno de **controle e acompanhamento de bugs**, desenvolvido para demonstrar o domínio de **operações CRUD completas** com **FastAPI** no backend e **HTML/CSS/JS puro** no frontend.  
O foco deste projeto é a **organização de código**, **boas práticas** e uma **interface funcional e elegante** — ideal para uso como **projeto de portfólio**.

---

## 🚀 Tecnologias utilizadas

### 🧠 Backend
- [FastAPI](https://fastapi.tiangolo.com/) — framework moderno e rápido para APIs REST.
- [Pydantic](https://docs.pydantic.dev/) — validação de dados e modelos.
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI leve e eficiente.
- [SQLite](https://www.sqlite.org/) — banco de dados simples e embutido.

### 🎨 Frontend
- HTML5 sem frameworks.
- CSS com tema **dark azul moderno**.
- JavaScript puro para consumo da API e manipulação do DOM.

---

## ⚙️ Funcionalidades principais

✅ **CRUD completo de bugs**:
- Criar novos bugs (status inicial: *Aberto*);
- Editar bugs existentes (com alteração de status para *Em andamento* ou *Resolvido*);
- Excluir bugs;
- Buscar bugs por título ou descrição.

✅ **Interface moderna e responsiva**:
- Layout escuro, centrado e visualmente agradável;
- Tabelas e botões estilizados;
- Textos claros e ícones de ação intuitivos.

✅ **Integração direta com a API FastAPI**:
- Comunicação via `fetch()` no frontend;
- Rotas REST (`GET`, `POST`, `PUT`, `DELETE`);
- Documentação automática da API via **Swagger** e **ReDoc**.

---

