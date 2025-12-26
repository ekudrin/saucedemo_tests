FROM python:3.10-slim

WORKDIR /app

# Установка chromium + chromedriver ОДНОЙ версии
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    default-jre \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Установка Allure
RUN curl -o allure.zip -Ls \
    https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.zip \
    && unzip allure.zip -d /opt/ \
    && ln -s /opt/allure-2.27.0/bin/allure /usr/bin/allure \
    && rm allure.zip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]
