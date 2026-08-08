from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pandas as pd
import joblib


app = FastAPI(title="Titanic Survival Prediction System")


# Load trained model
model = joblib.load("model.pkl")


# Templates
templates = Jinja2Templates(directory="templates")


# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Features used by the model
features = [
    "Passengerid",
    "Age",
    "Fare",
    "Sex",
    "sibsp",
    "Parch",
    "Pclass",
    "Embarked"
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": None
        }
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):

    form = await request.form()

    passenger_id = int(form["Passengerid"])
    age = float(form["Age"])
    fare = float(form["Fare"])
    sex = int(form["Sex"])
    sibsp = int(form["sibsp"])
    parch = int(form["Parch"])
    pclass = int(form["Pclass"])
    embarked = int(form["Embarked"])

    data = pd.DataFrame(
        [[
            passenger_id,
            age,
            fare,
            sex,
            sibsp,
            parch,
            pclass,
            embarked
        ]],
        columns=features
    )

    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "🟢 Passenger Survived"
    else:
        result = "🔴 Passenger Did Not Survive"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": result
        }
    )