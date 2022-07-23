#!/bin/bash

docker build -t pneuma/eltaskdag .

docker tag pneuma/eltaskdag:latest pneuma/eltaskdag:v1.0.0