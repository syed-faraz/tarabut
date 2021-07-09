FROM python:3.8-slim-buster

WORKDIR /app

COPY ./app/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app/app.py ./

CMD [ "FLASK_APP=app.py", "python3", "-m" , "flask", "run", "--host=0.0.0.0"]