#!/bin/sh
if [[ "$(id -u)" -ne 0 ]];
then
  echo "Please, Run This Program as Root!"
  exit
fi

function main() {
    printf '\033]2;Black-Database/Installing...\a'
    clear
    time_zone=date
    echo "Installing Black-Database..."
    chmod +x main.py
    chmod +x requiremments.txt
    sleep 2
    echo "Installing Python..."
    sleep 0.25
    apt install python
    apt install python3
    apt install python3-pip
    pip install --upgrade pip
    echo "
Finish At: $time_zone

Usage: python main.py"
"
    exit
}
main
