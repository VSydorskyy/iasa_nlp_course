import os
import transformers
from fastapi import FastAPI, Request


pipe = transformers.pipeline("text-classification", model=os.environ.get('MODEL_NAME'), device='cpu')

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.post("/classify")
async def classify(request: Request):
    # Retrieve the raw string from the request body
    data = await request.body()
    data_str = data.decode("utf-8")  # Decode bytes to string
    return pipe(data_str)[0]
