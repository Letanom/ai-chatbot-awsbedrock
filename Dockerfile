# Multi-stage build for the entire application
FROM node:16-alpine as frontend-build

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm ci --only=production --silent
COPY frontend/ .
RUN npm run build

FROM python:3.9-slim

WORKDIR /app

# Install nginx and supervisor in one layer
RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx supervisor curl && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Copy backend and install dependencies
COPY backend/ ./backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy frontend build
COPY --from=frontend-build /app/frontend/build /var/www/html

# Copy configs
COPY frontend/nginx.conf /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Create logs directory
RUN mkdir -p /var/log/supervisor

EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"] 