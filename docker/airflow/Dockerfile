# Use the official Airflow image as the base
FROM apache/airflow:latest

# Set the AIRFLOW_HOME environment variable
ENV AIRFLOW_HOME=/usr/local/airflow
WORKDIR ${AIRFLOW_HOME}

COPY airflow.cfg start.sh ./
USER root
RUN chmod +x start.sh

# Switch back to the airflow user
USER airflow

# Default entrypoint is "airflow"
ENTRYPOINT []