FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

COPY * /app/

RUN pip install -r requirements.txt

CMD ["bash"]
