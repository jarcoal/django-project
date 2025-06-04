FROM python:3.12

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# GDAL (uncomment as needed)
# RUN apt-get update -y
# RUN apt-get install -y gdal-bin python3-gdal

# set work directory
WORKDIR /usr/src/app

# Copy pipenv files in
COPY Pipfile .
COPY Pipfile.lock .

# Install pipenv
RUN pip install pipenv

# Install project dependencies
RUN pipenv install --dev --system --deploy

# copy project
COPY . .
