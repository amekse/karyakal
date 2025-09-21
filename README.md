# Karyakal

Karyakal is a modular and extendable platform developed as part of an academic research initiative.  
It focuses on **task evaluation, engineer efficiency, and intelligent matching of work units** in a scalable and reproducible environment.

## Features

- Custom KPI calculations for engineers and tasks  
- Lightweight data processing with Python  
- Configurable scoring logic for experimentation and tuning  
- Jupyter Notebook support for exploratory analysis  
- Clean architecture for integration into larger systems  
- Reproducible synthetic data generator  

## Tech Stack

- Python 3.12+  
- Jupyter Notebooks  
- VS Code (recommended)  
- Virtualenv for isolation  
- JSON-based data mocking  
- GitHub for version control  

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/amekse/karyakal.git
cd karyakal
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt