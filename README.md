# Simple AI App for processing PDFs

Welcome to the Streamlit Application! This README provides instructions on how to set up and run the application.

## Installation

1. Clone the repository

2. Put **your** `OPENAI_API_KEY` to `.env` file

```
OPENAI_API_KEY=<your-openai-api-key>
```

3. Create docker image:
```sh
docker build -t pdf_chat .
```
## Usage
Run docker container:
```sh
docker run -p 8501:8501 pdf_chat
```
When docker container is up go to
```commandline
http://0.0.0.0:8501
```

