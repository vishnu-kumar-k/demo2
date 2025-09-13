FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . .

# Run FastAPI on port 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
