#!/usr/bin/env python3
"""
Database initialization script for ZenGarden Backend
Creates the database and adds a default user if it doesn't exist
"""

import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.models import Base, User

def init_database():
    """Initialize the database and create default user"""
    
    # Ensure data directory exists
    os.makedirs("./data", exist_ok=True)
    
    # Create database engine
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    # Create session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        # Check if default user exists
        default_user = db.query(User).filter(User.username == "111").first()
        
        if not default_user:
            # Create default user
            hashed_password = get_password_hash("111")
            default_user = User(username="111", hashed_password=hashed_password)
            db.add(default_user)
            db.commit()
            print("✅ Default user '111' created successfully")
        else:
            print("ℹ️  Default user '111' already exists")
            
    except Exception as e:
        print(f"❌ Error creating default user: {e}")
        db.rollback()
    finally:
        db.close()
    
    print("✅ Database initialization completed")

if __name__ == "__main__":
    init_database() 