# Folosim imagine Python slim
FROM python:3.10-slim

# Director de lucru
WORKDIR /app

# Copiem dependintele
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul fisierelor
COPY . .

# Expunem portul Flask
EXPOSE 5000

# Rulam direct serverul Flask
CMD ["python3", "app/server.py"]

