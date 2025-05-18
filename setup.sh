#!/bin/bash

echo "🔧 Creating virtual environment..."
python3 -m venv env

echo "📦 Activating environment and installing dependencies..."
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Environment setup complete. You can now run:"
echo "source env/bin/activate"
echo "jupyter notebook"
