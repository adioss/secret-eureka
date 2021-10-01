FROM python:3.8-buster
RUN addgroup --gid 1000 changeme
RUN useradd -u 1000 -g 1000 changeme
RUN mkdir /home/changeme
COPY src /home/changeme/src
RUN chown -R changeme: /home/changeme
WORKDIR /home/changeme

RUN pip install --upgrade pip
RUN pip install pipenv
ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

WORKDIR /home/changeme/src
USER changeme

ENTRYPOINT ["python", "/home/changeme/src/main.py"]