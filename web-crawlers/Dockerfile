FROM python:3.6-slim-stretch
LABEL maintainer="rodion43pv@gmail.com>"

WORKDIR /usr/app/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --upgrade setuptools

RUN mkdir /etc/scrapyd/ \
    && echo "[scrapyd] \n bind_address = 0.0.0.0" > /etc/scrapyd/scrapyd.conf


EXPOSE 6800

# Run the command on container startup
CMD scrapyd && scrapyd-deploy
