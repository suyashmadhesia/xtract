#!/bin/bash
PWD="$(pwd)"
DIR="${PWD}/env"
RED='\033[0;31m'
GREEN="\033[0;32m"
ENDCOLOR="\033[0;m"
if [ -d "$DIR" ]; then
    echo -e "${GREEN}INFO: Virtual environment exists${ENDCOLOR}\n"
else
    echo -e "${GREEN}INFO: Virtual environment does not exist \n creating virtual environment... ${ENDCOLOR}\n"
    python3 -m venv env || python -m venv env
fi