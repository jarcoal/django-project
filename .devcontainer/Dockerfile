# Use the base image (change the version number if needed)
FROM mcr.microsoft.com/vscode/devcontainers/python:3.12

# Install Node.js (change the version number if needed)
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm

# Set the working directory
WORKDIR /usr/src/app
