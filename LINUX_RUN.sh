#!/bin/bash
sudo apt --yes install python3
sudo add-apt-repository universe
sudo apt --yes install python3-pip
sudo apt --yes install python3-venv
python3 -m venv env
source env/bin/activate
pip3 install flask selenium
sudo apt --yes install chromium-chromedriver
python3 webapp.py

