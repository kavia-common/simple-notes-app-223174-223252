# simple-notes-app-223174-223252

This repository contains a simple Notes backend built with FastAPI.

Quick start (backend):

```bash
cd notes_backend
pip install -r requirements.txt
uvicorn src.api.main:app --host 0.0.0.0 --port 3001 --reload
```

Open the API docs at:
- http://localhost:3001/docs
- http://localhost:3001/openapi.json