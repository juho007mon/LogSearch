#!/bin/bash

# Load variables from .env file
while read -r line || [[ -n "$line" ]]; do
    export "$line"
done < .env

# List of environment variables to check
L_VARIABLES=("ES_DIR" "ES_CONFIG")
# Check each variable
for VAR_NAME in "${L_VARIABLES[@]}"; do
  if [ -z "${!VAR_NAME}" ]; then
    echo "Error: $VAR_NAME is not set"
    exit 1
  fi
done

# Starting Elasticsearch with the specified configuration file
$ES_DIR/bin/elasticsearch -Epath.conf=$ES_CONFIG