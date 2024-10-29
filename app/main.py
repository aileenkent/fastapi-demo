#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

app = FastAPI()

@app.get("/")  # zone apex
def zone_apex():
    return {"Good Morning": "Sunshine! The Earth says Hello!"}

@app.get("/sum/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/multiply/{c}/{d}")
def multiply(c: int, d: int):
    return {"product": c * d}


@app.get("/quotient/{e}/{f}")
def divide(e: int, f: int):
    return{"quotient": e / f}

@app.get("/square/{g}")
def square(g: int):
    return{"squared": g ** 2}

@app.get("/difference/{h}/{i}")
def subtract(h: int, i: int):
    return{"difference": h - i}

@app.get("/customer/{idx}")
def customer(idx: int):
    #read data into a df
    df = pd.read_csv("customers.csv")
    #filter the data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@app.post("/get_body")
async def get_body(request: Request):
    response = await request.json()
    first_name = response["fname"]
    last_name = response["lname"]
    favorite_number = response["favnu"]
    return {"first_name": first_name, "last_name": last_name, "favorite_number": favorite_number}