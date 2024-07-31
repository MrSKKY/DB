#!/bin/bash

# Name of the screen session
SCREEN_NAME="server_screen"

# Path to your node executable
NODE_PATH=$(which node)

# Path to your server.js
SERVER_PATH=$(pwd)/server.js

# Debugging information
echo "Node path: $NODE_PATH"
echo "Server path: $SERVER_PATH"
echo "Starting server.js in a new screen session '$SCREEN_NAME'..."

# Start server.js in a new screen session
screen -dmS $SCREEN_NAME $NODE_PATH $SERVER_PATH

# Verify if the screen session was started
if screen -list | grep -q "$SCREEN_NAME"; then
    echo "Server started in screen session '$SCREEN_NAME'."
else
    echo "Failed to start the server in screen session '$SCREEN_NAME'."
fi
