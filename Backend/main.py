from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
import json
import os

app = FastAPI()

app.mount("/home", StaticFiles(directory="home", html=True), name="components")

current_temperature = ""

#This updates the current temperature when the esp sends it
@app.get("/set")
def set_message(msg: str):
    global current_temperature
    current_temperature = msg
    return {"stored": current_temperature}

@app.get("/temperature")
def pass_temperature():
  return {"temperature" : current_temperature}