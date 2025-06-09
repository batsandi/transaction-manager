FROM python:3.12-slim

WORKDIR /app

# Install netcat to check for db if is up to move along in the prestart script
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x /app/app/prestart.sh

CMD ["/bin/sh", "-c", "/app/app/prestart.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"]
