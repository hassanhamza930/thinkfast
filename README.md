# ThinkFast API

A minimal FastAPI application exposing a `/reason` endpoint.

## Usage

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn app.main:app --reload
```

Send a request to `/reason` with JSON body containing `api_key`, `model`, and `messages`.
