FROM python:3.12-slim

WORKDIR /app
COPY game.py .

CMD ["python", "game.py"]
