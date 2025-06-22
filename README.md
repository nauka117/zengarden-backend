# Zen Garden Backend

A FastAPI-based backend service for flower planning and management.

## Features

- FastAPI REST API
- SQLAlchemy ORM with SQLite database
- JWT authentication
- CORS support
- Docker containerization ready

## Quick Start

### Option 1: Docker (Recommended)

1. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

2. **Or build and run with Docker directly:**
   ```bash
   docker build -t zengarden-backend .
   docker run -p 8000:8000 zengarden-backend
   ```

3. **Access the API:**
   - API: http://localhost:8000
   - Documentation: http://localhost:8000/docs
   - Health check: http://localhost:8000/health

### Option 2: Local Development

1. **Create virtual environment:**
   ```bash
   # For bash/zsh
   python -m venv .venv
   source .venv/bin/activate
   
   # For fish shell
   python -m venv .venv
   source .venv/bin/activate.fish
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Development Setup

1. **Install development dependencies:**
   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Run tests:**
   ```bash
   pytest
   ```

3. **Format code:**
   ```bash
   black .
   ```

4. **Lint code:**
   ```bash
   flake8 .
   ```

## API Endpoints

- `GET /health` - Health check
- `GET /api/v1/` - API root
- `POST /api/v1/auth/login` - User login
- `GET /api/v1/flowers` - Get flowers
- `POST /api/v1/flowers` - Create flower

## Environment Variables

The application uses the following environment variables (with defaults):

- `SECRET_KEY`: JWT secret key (default: "your-secret-key-keep-it-secret")
- `ALGORITHM`: JWT algorithm (default: "HS256")
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration (default: 30)
- `SQLALCHEMY_DATABASE_URL`: Database URL (default: "sqlite:///./flowers.db")

## Troubleshooting

### IDE Package Installation Issues

If your IDE fails to install packages automatically:

1. **Ensure you're using the correct Python interpreter:**
   - Point your IDE to `.venv/bin/python`
   - For VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose `.venv/bin/python`

2. **For fish shell users:**
   - Use `source .venv/bin/activate.fish` instead of `source .venv/bin/activate`
   - Some IDEs may need manual configuration for fish shell

3. **Manual installation:**
   ```bash
   source .venv/bin/activate.fish  # or activate for bash
   pip install -r requirements.txt
   ```

### Docker Issues

1. **Build fails:**
   - Ensure Docker is running
   - Check if all files are present (Dockerfile, requirements.txt)
   - Try `docker system prune` to clear cache

2. **Port conflicts:**
   - Change the port in docker-compose.yml if 8000 is already in use
   - Use `docker-compose up -p 8001` to use a different port

3. **Database issues:**
   - The SQLite database file is mounted as a volume
   - Ensure the file has proper permissions

## Production Deployment

For production deployment:

1. **Use environment variables for secrets:**
   ```bash
   export SECRET_KEY="your-production-secret-key"
   export SQLALCHEMY_DATABASE_URL="postgresql://user:pass@host/db"
   ```

2. **Consider using PostgreSQL instead of SQLite:**
   - Uncomment the postgres service in docker-compose.yml
   - Update the database URL

3. **Add proper CORS origins:**
   - Update the CORS configuration in `app/main.py`

4. **Use a reverse proxy (nginx) for production**

## Project Structure

```
zengarden-backend/
├── app/
│   ├── api/v1/          # API endpoints
│   ├── core/            # Configuration and security
│   ├── db/              # Database setup
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   └── main.py          # FastAPI application
├── Dockerfile           # Docker configuration
├── docker-compose.yml   # Docker Compose setup
├── requirements.txt     # Production dependencies
├── requirements-dev.txt # Development dependencies
└── README.md           # This file
```
