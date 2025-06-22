# Troubleshooting Guide

## Problem: IDE Auto Package Installation Failed

### Root Causes Identified:

1. **Shell Compatibility Issue**: You're using fish shell, but most IDEs expect bash/zsh
2. **Version Constraints**: Original requirements.txt had strict version pins that may conflict
3. **Missing Dependencies**: Some packages needed for production weren't included

### Solutions Implemented:

#### 1. Fixed Virtual Environment Activation

**For fish shell users:**
```bash
# Use this instead of the regular activate script
source .venv/bin/activate.fish
```

**For IDE configuration:**
- Point your IDE to `.venv/bin/python` as the Python interpreter
- For VS Code: `Ctrl+Shift+P` → "Python: Select Interpreter" → Choose `.venv/bin/python`

#### 2. Updated Requirements.txt

- Changed from strict version pins (`==`) to flexible ranges (`>=`, `<`)
- Added `uvicorn[standard]` for better performance
- Added `python-dotenv` for environment variable management
- Organized dependencies with comments

#### 3. Created Development Tools

- **`setup_dev.sh`**: Automated setup script
- **`.vscode/settings.json`**: IDE configuration
- **`requirements-dev.txt`**: Development dependencies

## Problem: Docker Containerization Concerns

### Solutions Implemented:

#### 1. Dockerfile Best Practices

- Uses Python 3.11 (more stable than 3.13)
- Multi-stage build optimization
- Non-root user for security
- Health checks included
- Proper dependency caching

#### 2. Docker Compose Setup

- Easy development and deployment
- Volume mounting for database persistence
- Environment variable configuration
- Health check integration

#### 3. Docker Optimization

- `.dockerignore` file to reduce build context
- Layer caching optimization
- Minimal base image (python:3.11-slim)

## Quick Fix Commands

### For Immediate IDE Issues:

```bash
# 1. Ensure correct Python interpreter
which python  # Should point to .venv/bin/python

# 2. Reinstall packages if needed
source .venv/bin/activate.fish
pip install -r requirements.txt --upgrade

# 3. Test application
python -c "from app.main import app; print('✅ Success')"
```

### For Docker Setup:

```bash
# Install Docker (Arch Linux)
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER

# Build and run
docker-compose up --build
```

## Prevention Strategies

### 1. Use the Setup Script

```bash
# Basic setup
./setup_dev.sh

# With development tools
./setup_dev.sh --dev
```

### 2. IDE Configuration

- Always use the virtual environment Python interpreter
- Configure your IDE to use fish shell if needed
- Use the provided VS Code settings

### 3. Version Management

- Use flexible version constraints in requirements.txt
- Test with multiple Python versions
- Keep development and production requirements separate

## Common Issues and Solutions

### Issue: "case builtin not inside of switch block"
**Solution**: Use `source .venv/bin/activate.fish` instead of `source .venv/bin/activate`

### Issue: IDE can't find packages
**Solution**: 
1. Ensure IDE uses `.venv/bin/python`
2. Run `pip install -r requirements.txt` manually
3. Restart IDE after virtual environment activation

### Issue: Docker build fails
**Solution**:
1. Check if Docker is installed and running
2. Ensure all files are present (Dockerfile, requirements.txt)
3. Try `docker system prune` to clear cache

### Issue: Port conflicts
**Solution**:
1. Change port in docker-compose.yml
2. Use `docker-compose up -p 8001` for different port
3. Check if port 8000 is already in use

## Testing Your Setup

### 1. Local Development Test

```bash
source .venv/bin/activate.fish
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Docker Test

```bash
docker-compose up --build
```

### 3. Health Check

Visit: http://localhost:8000/health

Should return: `{"status": "healthy", "service": "Flower Planning Backend"}`

## Next Steps

1. **Install Docker** if you want containerization
2. **Set up environment variables** for production
3. **Configure your IDE** to use the virtual environment
4. **Test the application** with the provided endpoints
5. **Consider PostgreSQL** for production database

## Support

If you continue to have issues:

1. Check the logs in your IDE's output panel
2. Run the setup script: `./setup_dev.sh`
3. Verify Python interpreter path in your IDE
4. Test with the provided health check endpoint 