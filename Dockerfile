FROM python:3.6.10-alpine

# environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# working dir
RUN mkdir /code
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY entrypoint.sh /code/entrypoint.sh

# copy project
COPY . /code

# run entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]
