FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/Ilevk/optuna.git@d9fa004
RUN pip install PyMySQL psycopg2-binary cryptography redis pymssql

WORKDIR /work
