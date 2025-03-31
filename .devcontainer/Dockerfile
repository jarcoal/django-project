# Use the base image with the latest Python 3.12 version
FROM mcr.microsoft.com/devcontainers/python:1.2.1-3.12-bullseye

# Update the package list and upgrade all packages to the latest version
RUN apt-get update -y
RUN apt-get upgrade -y

# Install Node.js (change the version number if needed)
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm

# Set the working directory
WORKDIR /usr/src/app
