FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install

COPY . /app/

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["pipenv", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
