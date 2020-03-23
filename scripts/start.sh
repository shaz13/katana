#!/bin/bash
gunicorn --log-config ./configurations/logging.conf main:app \
         --bind 0.0.0.0:9000
