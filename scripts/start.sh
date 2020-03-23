#!/bin/bash
gunicorn --log-config ./config/logging.conf main:app \
         --bind 0.0.0.0:9000
