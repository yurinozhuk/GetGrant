FROM python:3
WORKDIR /app

COPY requirements.txt .
COPY web_tests .

# Додаємо шлях до каталогу web_tests у PYTHONPATH
ENV PYTHONPATH=/app/web_tests

RUN pip install --no-cache-dir -r requirements.txt

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
#CMD sh -c 'while sleep 3600; do :; done'
CMD ["pytest", "-v", "tests"]