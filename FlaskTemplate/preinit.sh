#!/bin/bash
sudo curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
sudo curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
sudo ACCEPT_EULA=Y apt-get install -y mssql-tools
sudo apt-get install -y build-essential
sudo echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
sudo source ~/.bashrc
sudo pip install pyodbc