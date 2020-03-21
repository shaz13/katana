#!/bin/bash
gunicorn main:app \
    --workers 4 \
    --bind 0.0.0.0:9000 \
    --log-file ./logs/katana.log
    --log-level DEBUG \
    --reload