#!/bin/zsh

python makemigrations
python migrates
python runserver 0.0.0.0:8000