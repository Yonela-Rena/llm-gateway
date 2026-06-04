# LLM Gateway API

A beginner-friendly FastAPI project that simulates an AI chat gateway. The project demonstrates API development, request validation, modular project structure, error handling, and API documentation using FastAPI.

## Features

* FastAPI backend
* Chat endpoint
* JSON responses
* Error handling
* Modular folder structure
* Swagger API documentation

## Project Structure

```bash
llm-gateway/
│
├── app/
│   ├── models/
│   │   └── response_model.py
│   │
│   ├── services/
│   │   └── ai_service.py
│   │
│   └── main.py
│
├── screenshots/
│   ├── swagger-docs.png
│   └── chat-response.png
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Yonela-Rena/llm-gateway.git
```

Go into the project folder:

```bash
cd llm-gateway
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

## API Endpoint

### POST `/chat`

Request:

```json
{
  "message": "Hello AI"
}
```

Response:

```json
{
  "response": "AI Response: You said -> Hello AI",
  "status": "success"
}
```

## API Docs

FastAPI automatically provides Swagger documentation:

```bash
http://127.0.0.1:8000/docs
```

## Screenshots

### Swagger Documentation

![Swagger Docs](screenshots/swagger-docs.png)

### Chat Endpoint Response

![Chat Response](screenshots/chat-response.png)

## Future Improvements

* Connect to real LLM APIs
* Add authentication
* Docker support
* Deployment
* Database integration

## Author

**Yonela Mhloluvele**

BSc Chemistry & Computer Science
Aspiring AI Engineer
