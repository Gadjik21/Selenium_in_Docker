# Базовый образ Python
FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install -r req.txt

# Установка хром драйвера
RUN apt update -y && apt-get install -y wget unzip &&  \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

CMD ["python", "main.py"]
