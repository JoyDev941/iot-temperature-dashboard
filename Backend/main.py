from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from datetime import datetime
import psycopg2
import json
import os

app = FastAPI()

app.mount("/home", StaticFiles(directory="home", html=True), name="components")


def get_connection():

    return psycopg2.connect(
        host = "localhost",
        database="tempdb",#
        user="lan_serv",#
        password="esptemp32"#
    )

@app.get("/")
def root():
    return RedirectResponse("/home")


@app.on_event("shutdown") # when we close server it will first close the database connection and then shutdown
def shutdown_event():
    print("Server is shutting down...")


#This updates the current temperature when the esp sends it + stores it in database
@app.get("/set") # format of url is: http://IPAddress/set?temp=25&hum=60
def set_message(temp: str, hum: str):

    global current_temperature
    current_temperature = temp

    global current_humidity
    current_humidity = hum

    try:
        con = get_connection()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s);",
            (current_temperature, current_humidity)
        )

        con.commit()
        cur.close()
        con.close()

    except Exception as e:
        return {"error": str(e)}

    return {"stored": current_temperature, "humidity": current_humidity}



#send temperature reading to front end JS script
@app.get("/temperature")
def pass_temperature():
    return {"temperature" : current_temperature}
