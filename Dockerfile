FROM python:3.14.0rc1-slim-bullseye
WORKDIR /usr/src/app
RUN apt-get update
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "./update-dns.py" ]