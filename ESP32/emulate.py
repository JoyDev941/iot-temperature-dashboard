import requests
import time

url = "http://192.168.68.120:2004/set?msg=12"

try:
    while True:
        response = requests.get(url)
        print(f"Sent 12 → Status: {response.status_code}, Response: {response.text}")
        time.sleep(1)  # wait 1 second between requests
except KeyboardInterrupt:
    print("\nLoop stopped by user")