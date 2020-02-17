#!/bin/bash
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
pip3 install flask selenium
python3 webapp.py

