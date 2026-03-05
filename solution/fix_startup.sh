sed -i 's/python app.py/uvicorn app:app --host 0.0.0.0 --port 8000/' /app/start.sh
chmod +x /app/start.sh
