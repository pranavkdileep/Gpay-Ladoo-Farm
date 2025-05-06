FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]