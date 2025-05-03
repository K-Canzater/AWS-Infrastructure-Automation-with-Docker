FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY stop/stop-instances.py .

ENV INSTANCE_IDS=""

CMD ["python", "stop-instances.py"]