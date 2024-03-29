##########################################
# Python
##########################################
FROM python:3.11.2-slim AS python

# Create app directory
WORKDIR /usr/src/app

# Install packages
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt


##########################################
# App
##########################################
FROM python AS todo

ENTRYPOINT [ "python", "./todo" ]
