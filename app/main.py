#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
<<<<<<< HEAD
    return {"Hello": "Aileen"}
=======
    return {"Good Day": "Sunshine!"}
>>>>>>> bd87238d5caaf0e395b86e524ade0dc51b305bcc

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
<<<<<<< HEAD
    return {"product": c * d}

=======
    return {"product": c * d}
>>>>>>> bd87238d5caaf0e395b86e524ade0dc51b305bcc
