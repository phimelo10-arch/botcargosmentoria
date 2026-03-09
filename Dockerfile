
FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY meubot.py .


CMD ["python", "-u", "meubot.py"]
