# Build an Analytics API using FastAPI + Time-series Postgres

Start by building an Analytic API service with Python,FastAPI, and Time-series Postgres with TimescaleDB.

## Docker

- 'docker build -t analytics-api -f Dockerfile.web .'
- 'docker run'

becomes 

- 'docker compose up --watch'
- 'docker compose down' or 'docker compose down -v' (to remove volumes)
- 'docker compose run app /bin/bash' or 'docker compose run app python'
