#!/bin/bash

echo "Waiting for PostgreSQL to start..."

# We use a loop with 'nc' (netcat) to check if the database port is open.
# while ! nc -z db 5432; do
#   sleep 0.1
# done

echo "PostgreSQL started."

# Run the Python script to create the initial tables and data.
python -m app.initial_data
