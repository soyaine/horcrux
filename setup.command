#!/usr/bin/env bash

SCRIPT_PATH=$(dirname "$0")

eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv activate p
pyenv version
pip install pyyaml
pip install Pillow

python $SCRIPT_PATH/scripts/main.py
