@echo off

echo Setting up Python Environment...


REM Create virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate


echo Installing Requirements...

pip uninstall -r requirements.txt -y
pip install -r requirements.txt


echo Starting FastAPI App...

start "" "http://127.0.0.1:8000"
uvicorn app:app --port 8000
