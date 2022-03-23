FROM python:3.9

WORKDIR /code

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN apt-get update && apt-get -y install gcc librdkafka-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]
