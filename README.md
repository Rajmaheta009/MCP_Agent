# 🤖 Raj Assistant MCP

> A modular AI Assistant built using the **Model Context Protocol (MCP)** that provides calculator, weather, news, AI chat, currency conversion, document processing, and future RAG capabilities.

---

# 📌 Overview

Raj Assistant MCP is a production-style MCP Server built with Python.

The goal of this project is to learn and demonstrate the complete MCP ecosystem by creating a modular AI assistant that can expose multiple tools to any MCP-compatible AI client such as:

- MCP Inspector
- Claude Desktop
- VS Code MCP
- Cursor AI
- Future MCP Clients

Instead of placing every tool inside one file, this project follows a scalable architecture similar to real backend applications.

---

# 🚀 Features

## ✅ Current Features

- Calculator
    - Add
    - Subtract
    - Multiply
    - Divide

- Date & Time
    - Current Date
    - Current Time
    - Current DateTime

- Modular Architecture

- MCP Inspector Support

- Environment Configuration (.env)

---

## 🚧 Upcoming Features

### Weather

- Current Weather
- Forecast
- Humidity
- Wind Speed

### News

- Top Headlines
- Category News
- Country News

### AI Chat

- OpenAI
- Gemini
- Ollama
- OpenRouter

### Currency

- Currency Conversion
- Exchange Rates

### File Processing

- PDF Reader
- DOCX Reader
- Excel Reader
- Image Reader

### Database

- PostgreSQL
- MongoDB
- SQLite

### RAG

- Vector Database
- Embeddings
- Document Chat

### AI Agent

- Automatic Tool Selection
- Multi-step Reasoning
- Tool Chaining

---

# 📂 Project Structure

```
AI_MCP/
│
├── .venv/
│
├── server.py
├── config.py
├── requirements.txt
├── README.md
├── .env
│
├── tools/
│   ├── __init__.py
│   ├── calculator.py
│   ├── datetime.py
│   ├── weather.py
│   ├── news.py
│   ├── currency.py
│   ├── chat.py
│   ├── pdf.py
│   ├── excel.py
│   └── image.py
│
├── services/
│   ├── __init__.py
│   ├── weather_service.py
│   ├── news_service.py
│   ├── ai_service.py
│   ├── currency_service.py
│   └── pdf_service.py
│
├── database/
│   ├── postgres.py
│   ├── mongodb.py
│   └── sqlite.py
│
├── rag/
│   ├── embedding.py
│   ├── vector_store.py
│   └── retriever.py
│
├── utils/
│   ├── logger.py
│   ├── helper.py
│   └── validator.py
│
└── tests/
```

---

# 🏗 Architecture

```
                User

                  │

                  ▼

          MCP Client
 (Inspector / Claude / Cursor)

                  │

                  ▼

          Raj Assistant MCP

                  │

      ┌───────────┼────────────┐
      │           │            │
      ▼           ▼            ▼

 Calculator   Weather      AI Chat

      │           │            │
      ▼           ▼            ▼

 Services    Services    AI Services

      │           │            │
      ▼           ▼            ▼

 External APIs / Database / AI Models
```

---

# 🔄 MCP Workflow

```
User

↓

MCP Client

↓

tools/list

↓

Raj Assistant

↓

Available Tools

↓

AI Chooses Tool

↓

tools/call

↓

Python Function

↓

Response

↓

AI

↓

User
```

---

# 🧠 Learning Objectives

This project demonstrates:

- Model Context Protocol (MCP)
- Modular Software Architecture
- Python Development
- API Integration
- AI Integration
- Service Layer Pattern
- Environment Configuration
- Tool Registration
- MCP Inspector
- RAG Architecture
- AI Agent Design

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI_MCP.git

cd AI_MCP
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
PROJECT_NAME=Raj Assistant
VERSION=1.0.0

WEATHER_BASE_URL=https://api.open-meteo.com/v1/forecast

NEWS_API_KEY=

OPENAI_API_KEY=

GEMINI_API_KEY=

OPENROUTER_API_KEY=

OLLAMA_BASE_URL=http://localhost:11434
```

---

# ▶️ Run the Server

```bash
python server.py
```

or

```bash
mcp dev server.py
```

---

# 🧪 Testing with MCP Inspector

Launch Inspector

```bash
mcp dev server.py
```

Open the provided localhost URL in your browser.

Available tools will appear automatically.

Example:

```
add(10,20)

Result

30
```

---

# 📚 Technology Stack

### Backend

- Python 3.12+

### MCP

- Model Context Protocol SDK

### AI

- OpenAI
- Gemini
- Ollama
- OpenRouter

### APIs

- Open-Meteo
- News API

### Database

- PostgreSQL
- MongoDB
- SQLite

### RAG

- ChromaDB
- FAISS

---

# 🚀 Roadmap

## Phase 1

- ✅ Calculator
- ✅ Date & Time
- ✅ Modular Architecture

---

## Phase 2

- Weather API
- News API
- Currency API

---

## Phase 3

- AI Chat

---

## Phase 4

- PDF Reader
- Excel Reader
- Image Reader

---

## Phase 5

- PostgreSQL
- MongoDB

---

## Phase 6

- RAG

---

## Phase 7

- AI Agent

---

## Future Improvements

- Authentication
- Logging
- Docker Support
- Async Tools
- Streaming Responses
- Tool Permissions
- Multi-Agent Support
- Web Dashboard
- REST API Gateway

---

# 👨‍💻 Author

**Raj Ashvinkumar Maheta**

MCA Student | Python Developer | AI & MCP Enthusiast

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

🐛 Report issues

💡 Suggest improvements

---

# 📄 License

This project is licensed under the MIT License.

---

## 💙 Thank You

Happy Coding 🚀

Let's build the future of AI with MCP!