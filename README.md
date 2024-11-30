# Digital Theatre (digital-theatre)

A FastAPI backend service for hosting theatrical plays with AI voice-over capabilities.

## Features

- Play content management
- Character information
- AI voice-over generation
- Text synchronization with audio

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Activate virtual environment:
```bash
poetry shell
```

3. Run the development server:
```bash
uvicorn src.main:app --reload
```

## Project Structure

```
backend/
├── src/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── tests/
├── pyproject.toml
└── README.md
```

## License

MIT