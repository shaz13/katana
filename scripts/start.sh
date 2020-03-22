#!/bin/bash
gunicorn --log-config gunicorn_logging.conf main:app \
         --bind 0.0.0.0:9000
