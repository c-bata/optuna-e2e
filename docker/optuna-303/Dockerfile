FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/c-bata/optuna.git@make-migration-script-faster
RUN pip install PyMySQL psycopg2-binary cryptography redis pymssql

WORKDIR /work
