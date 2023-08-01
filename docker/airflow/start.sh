#!/bin/bash

# Should start after database
airflow db init
airflow users create  \
    --username admin  \
    --password admin  \
    --firstname Admin  \
    --lastname Adminov  \
    --role Admin  \
    --email admin@example.com