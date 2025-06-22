#!/bin/bash

# Development setup script for Zen Garden Backend
# This script helps set up the development environment

set -e

echo "🚀 Setting up Zen Garden Backend development environment..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or later."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "📦 Python version: $(python3 --version)"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🔧 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Install development dependencies if requested
if [ "$1" = "--dev" ]; then
    echo "📦 Installing development dependencies..."
    pip install -r requirements-dev.txt
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the virtual environment:"
echo "  source .venv/bin/activate"
echo ""
echo "To run the application:"
echo "  uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "To install Docker later:"
echo "  # For Arch Linux:"
echo "  sudo pacman -S docker docker-compose"
echo "  sudo systemctl enable --now docker"
echo "  sudo usermod -aG docker $USER"
echo ""
echo "Then you can use:"
echo "  docker-compose up --build" 