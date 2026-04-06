# IOT-Temperature-Dashboard

A fastAPI based service, that monitors the temperature sent from a ESP connected to a DHT11 (reads humidity and temperature) module.

## Features
- REST API built with FastAPI
- Dockerized for portability (In progress)
- Reverse proxied with NGINX
- CI/CD with GitHub Actions
- Designed for cloud deployment

## Architecture

Client → NGINX → FastAPI

- NGINX handles incoming traffic
- FastAPI processes requests
- Docker containers manage services

## Tech Stack
- FastAPI
- Docker
- NGINX
- GitHub Actions
- AWS EC2 (or Raspberry Pi)

# installation and setup
1 - clone the repository https://github.com/JoyDev941/iot-temperature-dashboard.git
2 - The Backend folder contains the script for the service, The ESP32 folder, contains the script for sending data.
3 - It is required to have a reserved/static address for the machine that will host the machine.
4 - The ESP32 script, must be modified ; the SSID, Password and the Reserved IP address of the host server.
5 - Make sure to run "./setup.sh" before running the script, otherwise NGINX is not going to work.
6 - In the Backend folder (stored in the server), run "uvicorn main:app --host RESERVERIP --port 8080".
7 - from the browser, of any device in your local network, search "http://RESERVERDIP" which is where the web interface is hosted.
8A - Paste the ESP32 Script in the Arduino IDE and flash it to your ESP32 connected to the ESP32 module.
8B - If the case that you do no have a ESP32, do not worry, Run the Python file "emulate.py" in your PC, to get data sent to the web app.

## Future Improvements
- Add authentication
- Scale with Kubernetes
- Add database
- make docker application
- use monitoring software such as Prometheus and Grafana

## Contributing
Pull requests are welcome.
