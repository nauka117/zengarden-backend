#!/bin/bash

# Initialize database
echo "🔧 Initializing database..."
python init_db.py

# Start the application
echo "🚀 Starting ZenGarden Backend..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 