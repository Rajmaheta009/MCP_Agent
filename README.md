# 🤖 Raj Assistant MCP

A modular **Model Context Protocol (MCP)** server built with Python. This project is designed to work with MCP Inspector and other MCP-compatible clients.

## What is implemented

- Calculator: add, subtract, multiply, divide, percentage
- Date/time with IANA timezones
- Current weather using Open-Meteo
- News using NewsData.io
- Currency conversion using Frankfurter
- Gemini AI chat
- PDF, DOCX, TXT, MD, CSV, XLSX and basic image file reading
- Local RAG document indexing and semantic search with ChromaDB
- Clean service/tool separation
- Environment-based configuration
- Basic tests

## Architecture

```text
MCP Client / Inspector
        |
        v
   server.py
        |
        +-------------------+
        |                   |
     MCP Tools          Services
        |                   |
        +---------+---------+
                  |
       External APIs / Chroma
                  |
              Local files
```

## 1. Setup on Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` and add your own `NEWS_API_KEY` and `GEMINI_API_KEY`.

> **Security:** The old uploaded project contained API keys in `.env`. Rotate/revoke those keys and never commit `.env` to Git.

## 2. Run normally

```powershell
python server.py
```

The MCP server uses stdio, so it may appear to wait without printing a normal web page.

## 3. Run MCP Inspector

```powershell
mcp dev server.py
```

Then open the Inspector URL printed in the terminal.

If you get `ModuleNotFoundError`, activate the virtual environment in the same PowerShell window before running the command.

## 4. Tools

### Calculator
- `add`
- `subtract`
- `multiply`
- `divide`
- `percentage`

### Date/time
- `current_date`
- `current_time`
- `current_datetime`

Default timezone is `Asia/Kolkata`. You can pass another IANA timezone such as `UTC` or `America/New_York`.

### Weather

```text
get_current_weather(latitude=21.1702, longitude=72.8311)
```

Open-Meteo does not require an API key.

### News

Requires `NEWS_API_KEY`.

```text
top_news(topic="technology", country="in", limit=5)
```

### Currency

```text
convert_currency(amount=100, from_currency="USD", to_currency="INR")
```

Uses Frankfurter's public exchange-rate API.

### AI chat

Requires `GEMINI_API_KEY`.

```text
chat(message="Explain MCP in simple words")
```

### Documents

```text
read_document(path="C:\\path\\to\\file.pdf")
index_document(path="C:\\path\\to\\file.pdf")
search_knowledge(query="What is this document about?", top_k=5)
```

Supported: PDF, DOCX, TXT, MD, CSV, XLSX, JSON and basic image metadata.

## 5. Project structure

```text
project_mcp/
├── .env.example
├── config.py
├── server.py
├── requirements.txt
├── README.md
├── tools/
│   ├── calculator.py
│   ├── chat.py
│   ├── currency.py
│   ├── datetime.py
│   ├── documents.py
│   ├── news.py
│   ├── rag.py
│   └── weather.py
├── services/
│   ├── ai_service.py
│   ├── currency_service.py
│   ├── document_service.py
│   ├── rag_service.py
│   ├── news_service.py
│   └── weather_service.py
└── tests/
```

## Next stage: AI Agent

The MCP server is now a strong tool layer. An **AI Agent** should normally live in an MCP client/agent application that:
1. discovers tools with `tools/list`
2. sends the available tools to the model
3. lets the model choose a tool
4. calls the selected MCP tool with `tools/call`
5. feeds the result back to the model
6. repeats until the final answer is ready

This keeps the MCP server focused on reliable capabilities instead of mixing agent orchestration into every tool.

## License

MIT
