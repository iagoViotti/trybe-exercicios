FROM python:3-alpine3.17

WORKDIR /src

# Dica: instale primeiro as dependências antes de copiar todo o projeto
COPY src/*requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Esse argumento será passado dentro do docker-compose
ARG FLASK_ENV
RUN if ['FLASK_ENV' = 'dev'] ; then pip install --no-cache-dir -r requirements-dev; fi

COPY ./src .

CMD ["python", "app.py"]
