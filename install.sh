#!/bin/sh

if [[ "$(id -u)" -ne 0 ]];
then
  echo "
Please, Run Black-Attacker as Root!
"
  exit 
fi

function install() {
    printf '\033]2;Black-attacker/Installing\a'
    clear
    echo "Installing..."
    chmod +x black.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip install --upgrade pip
    sleep 0.25
    echo "
Finish...
Usage: 
     bash install.sh start
     
     or 
     
     python black.py
"
    sleep 0.25
    exit 
}
function start() {
    sleep 0.25
    chmod +x black.py
    python black.py
}
if [[ $1 == 'start' || $1 == '--start' ]];
then
  start
elif [[ $1 == '--help' || $1 == 'help' ]];
then
  echo "
Black-attacker Argument:
            --help
            --start
            --install
"
elif [[ $1 == '--install' || $1 == 'install ']];
then
  install
else
  echo "Usage: --help"
  exit
fi