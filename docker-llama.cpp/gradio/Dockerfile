FROM python:3.9-slim

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir gradio requests

EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "run_gradio.py"]
