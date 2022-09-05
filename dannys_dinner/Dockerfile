FROM python:3.10.4

WORKDIR /code

COPY ./requeriments.txt /code/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/requeriments.txt

COPY ./app /code/app

CMD ["python3", "/code/app/main.py"]

