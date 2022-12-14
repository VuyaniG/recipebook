FROM python:3
RUN mkdir /code

WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /code/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]