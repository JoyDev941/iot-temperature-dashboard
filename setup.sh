#!/bin/bash

echo "Updating packages..."
sudo apt update -y

echo "Checking if NGINX is installed..."
if ! command -v nginx &> /dev/null
then
    echo "NGINX not found. Installing..."
    sudo apt install nginx -y
else
    echo "NGINX already installed."
fi

echo "Creating systemd service..."

sudo bash -c 'cat > /etc/systemd/system/myapp.service <<EOF
[Unit]
Description=FastAPI Uvicorn App
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/your-project-folder
ExecStart=/usr/bin/python3 -m uvicorn app:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
EOF'

echo "Reloading systemd..."
sudo systemctl daemon-reexec
sudo systemctl daemon-reload

echo "Enabling FastAPI service..."
sudo systemctl enable myapp
sudo systemctl restart myapp

echo "Enabling and starting NGINX..."
sudo systemctl enable nginx
sudo systemctl restart nginx

echo "Setup complete 🚀"