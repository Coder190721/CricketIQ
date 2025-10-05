#!/usr/bin/env python3
"""
CricketIQ Setup Script
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False

def setup_cricket_iq():
    """Setup CricketIQ environment"""
    print("🏏 CricketIQ Setup")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    # Create .env file if it doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists("env_example.txt"):
            run_command("cp env_example.txt .env", "Creating .env file from example")
            print("📝 Please edit .env file and add your Google API key")
        else:
            print("⚠️  No env_example.txt found, please create .env manually")
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your Google API key")
    print("2. Run: python cricket_gradio_app.py")
    print("3. Open your browser to http://127.0.0.1:7891")
    
    return True

if __name__ == "__main__":
    setup_cricket_iq()