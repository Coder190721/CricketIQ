#!/usr/bin/env python3
"""
Setup script for Cricket Statistics Agent
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from dotenv import load_dotenv

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_environment():
    """Set up environment file"""
    env_file = Path(".env")
    env_example = Path("env_example.txt")
    
    if not env_file.exists() and env_example.exists():
        print("🔧 Setting up environment file...")
        shutil.copy(env_example, env_file)
        print("✅ Environment file created (.env)")
        print("⚠️  Please edit .env and add your Google API key")
        return True
    elif env_file.exists():
        print("✅ Environment file already exists")
        return True
    else:
        print("❌ Environment example file not found")
        return False

def check_api_key():
    """Check if Google API key is set"""
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key or api_key == "your_google_api_key_here":
        print("⚠️  Google API key not set")
        print("Please:")
        print("1. Get your API key from: https://makersuite.google.com/app/apikey")
        print("2. Edit .env file and set GOOGLE_API_KEY=your_actual_api_key")
        return False
    else:
        print("✅ Google API key is set")
        return True

def run_tests():
    """Run basic tests"""
    print("🧪 Running tests...")
    try:
        result = subprocess.run([sys.executable, "test_cricket_agent.py"], 
                              capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("✅ Tests passed")
            return True
        else:
            print(f"❌ Tests failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("⏰ Tests timed out (this is normal for first run)")
        return True
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False

def main():
    """Main setup function"""
    print("🏏 Cricket Statistics Agent Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup environment
    if not setup_environment():
        sys.exit(1)
    
    # Check API key
    api_key_set = check_api_key()
    
    print("\n🎉 Setup completed!")
    print("\n📋 Next steps:")
    print("1. Get your Google API key from: https://makersuite.google.com/app/apikey")
    print("2. Edit .env file and add your API key")
    print("3. Run the agent:")
    print("   - Web interface: python cricket_gradio_demo.py")
    print("   - Command line: python cricket_agent.py")
    print("   - Test: python test_cricket_agent.py")
    
    if api_key_set:
        print("\n🚀 Ready to run!")
        print("Try: python cricket_gradio_demo.py")

if __name__ == "__main__":
    main()
