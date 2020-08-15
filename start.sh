#! /bin/bash

gunicorn -w 3 -b :6000 run:app
