#!/bin/bash


echo "Loading... !"
sleep 0.3
python3 config.py
sleep 0.2
source backend/bin/activate
python3 main.py


deactivate
