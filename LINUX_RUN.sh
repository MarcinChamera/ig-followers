#!/bin/bash
sudo apt -y install python3-venv
python3 -m venv env
source env/bin/activate
pip3 install flask selenium
python3 webapp.py

