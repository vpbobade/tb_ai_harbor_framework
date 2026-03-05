FROM python:3.12-slim

WORKDIR /app

COPY * /app/

RUN pip install fastapi==0.95.0 uvicorn==0.22.0 sqlalchemy==2.0.0

CMD ["bash","start.sh"]
