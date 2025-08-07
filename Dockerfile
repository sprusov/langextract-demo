FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir .

RUN pip install --no-cache-dir pytest ruff

CMD ["python", "-m", "langextract_demo"]
