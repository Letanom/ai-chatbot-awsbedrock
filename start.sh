#!/bin/bash

# Start nginx
service nginx start

# Start Flask backend
cd /app/backend
python backend_api.py 