#!/bin/bash
# Avoid shifting paramters in second line, incompatible with Windows WSL2, Docker on windows
gunicorn --log-config ./configurations/logging.conf main:app --bind 0.0.0.0:9000
