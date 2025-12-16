# Notes Backend (FastAPI)

A simple FastAPI backend providing CRUD operations for notes using in-memory storage.

## Run locally

Requires Python 3.10+.

Install dependencies:
```bash
pip install -r requirements.txt
```

Start the server on port 3001:
```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 3001 --reload
```

Open API docs:
- Swagger UI: http://localhost:3001/docs
- OpenAPI JSON: http://localhost:3001/openapi.json

## Health
```bash
curl -s http://localhost:3001/
```

## Notes API

Create:
```bash
curl -s -X POST http://localhost:3001/notes \
  -H "Content-Type: application/json" \
  -d '{"title":"First Note","content":"Hello world"}'
```

List:
```bash
curl -s http://localhost:3001/notes
```

Get by ID:
```bash
curl -s http://localhost:3001/notes/1
```

Update:
```bash
curl -s -X PUT http://localhost:3001/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","content":"Updated content"}'
```

Delete:
```bash
curl -s -X DELETE http://localhost:3001/notes/1 -i
```

## Notes

- This service uses in-memory storage and will reset on restart.
- The code is structured to allow swapping the storage layer with a database in the future.
