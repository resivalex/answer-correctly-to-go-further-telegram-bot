#!/bin/bash +x

set -e

poetry update
poetry run python src/bot.py
