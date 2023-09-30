#!/bin/bash
SCRIPT_DIR="$(pwd)/scripts"
${SCRIPT_DIR}/env.sh
SCR="$(pwd)/env/bin/activate"
if [ -e "$SCR" ]
then
    source $(pwd)/env/bin/activate
else
    source $(pwd)/env/Scripts/activate
fi

RED='\033[0;31m'
GREEN="\033[0;32m"
ENDCOLOR="\033[0;m"

if [ "$#" -lt 2 ]
then 
  echo -e "${RED}ERROR: command usage './pacman <command> <package1> <package2> ...${ENDCOLOR}'"
  exit 1
fi

command="$1"
shift  # Remove the first argument (the command)
packages=("$@")

if [ "$command" == "install" ]
then
  for package in "${packages[@]}"
  do
    pip install "$package"
    if pip install "$package" &>/dev/null
    then
      pkg=$(pip freeze | grep -i "${package}=")
      if grep -Fq "$pkg" requirements.txt
      then
        echo -e "${GREEN}INFO: Skipping entry in requirements.txt ${ENDCOLOR}"
      else
        echo -e "${GREEN}INFO: Adding entry in requirements.txt ${ENDCOLOR}"
        pip freeze | grep -i "$package" >> requirements.txt
      fi
    else
      echo "Error: Failed to install package '$package'"
    fi
  done
elif [ "$command" == "uninstall" ]
then
  for package in "${packages[@]}"
  do
    pip uninstall "$package" -y
    # Remove the package from requirements.txt if it exists
    sed -i "/$package/d" requirements.txt
  done
fi

exit 0
