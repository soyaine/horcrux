#!/usr/bin/env bash

SCRIPT_PATH=$(dirname "$0")

python3 -m venv venv    
source venv/bin/activate  
pip install pyyaml
pip install Pillow
echo $VIRTUAL_ENV

python $SCRIPT_PATH/scripts/main.py
