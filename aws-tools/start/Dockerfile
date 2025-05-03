FROM python:3.13-slim

WORKDIR /app

# 1) install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2) add your start script
COPY start/start-instances.py .

ENV INSTANCE_IDS=""
CMD ["python", "start-instances.py"]
