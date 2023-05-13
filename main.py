import subprocess
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
from fastapi import FastAPI
import pandas as pd 

df = pd.read_csv('./data/smallDiagnosis2019.csv', low_memory=False)

app = FastAPI()

@app.get("/")
async def root():
    return {df.to_json(orient="records")}
