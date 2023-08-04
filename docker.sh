#!/bin/bash
docker build ./ -t flask-form
echo "view the container at http://0.0.0.0:5000/"
docker run -p 5000:5000 flask-form

