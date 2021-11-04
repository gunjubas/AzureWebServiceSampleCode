#!/bin/bash

if [ ! -f /tmp/myfile ]
then
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
    curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
    apt-get update
    ACCEPT_EULA=Y apt-get install -y msodbcsql17
    ACCEPT_EULA=Y apt-get install -y mssql-tools
    apt-get install -y build-essential
    echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
    source ~/.bashrc
    source "antenv"/bin/activate
    pip install pyodbc
    touch /tmp/myfile
else
    echo "Looks like all packages present. Nothing to do"
fi