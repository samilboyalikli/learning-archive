FROM python:3.12-slim

WORKDIR /consumer

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
