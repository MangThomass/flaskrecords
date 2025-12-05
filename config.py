<<<<<<< HEAD
import os

class Config:
    """Base configuration"""
    # Secret key for sessions and CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-change-in-production'
    
    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    
    # Disable modification tracking (saves resources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
=======
import os

class Config:
    """Base configuration"""
    # Secret key for sessions and CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-change-in-production'
    
    # SQLAlchemy database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    
    # Disable modification tracking (saves resources)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
>>>>>>> 4eea04cc5b8ab6a74f0a65f3a68c4f6f847b7739
