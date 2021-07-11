FROM python:3.8-slim-buster

WORKDIR /app

RUN useradd -m -r tarabut

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py .

RUN chown -R tarabut:tarabut /app

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

USER tarabut