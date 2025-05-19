#!/bin/bash

# Step 1: Install dependencies with pipenv
echo "Installing dependencies with pipenv..."
pipenv install --dev

# Step 2: Configure Git safe directory using the DevContainer's environment variable
echo "Configuring Git to trust the directory $WORKSPACE"
git config --global --add safe.directory ${containerWorkspaceFolder}

# Step 3: Add 'll' command to the environment for future terminal sessions
echo "Adding 'll' command to the environment"
echo "alias ll='ls -la --color=auto'" >> ~/.bashrc

# Reload the shell to make the new alias available in the current session
source ~/.bashrc

echo "Setup complete!"