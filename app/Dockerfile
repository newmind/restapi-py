FROM python:3.7

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000
CMD python app.py
#CMD python -m flask run --host=0.0.0.0
