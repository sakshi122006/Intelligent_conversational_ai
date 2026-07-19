FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y build-essential default-libmysqlclient-dev unixodbc-dev \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt
COPY . /app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
