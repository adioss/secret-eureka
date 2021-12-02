FROM python:3.8-buster
RUN addgroup --gid 1000 unconcealment
RUN useradd -u 1000 -g 1000 unconcealment
RUN mkdir /home/unconcealment
COPY unconcealment /home/unconcealment

WORKDIR /home/unconcealment

RUN pip install --upgrade pip
RUN pip install poetry
ADD pyproject.toml .
ADD poetry.lock .
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
RUN chown -R unconcealment: /home/unconcealment

# TODO remove that
#USER unconcealment

ENTRYPOINT ["poetry", "run", "python", "unconcealment/main.py"]