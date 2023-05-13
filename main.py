import subprocess
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
from fastapi import FastAPI
import pandas as pd
import numpy as np

df = pd.read_csv('./data/smallDiagnosis2019.csv')
df.replace('', np.nan, inplace=True) # replace empty with nan (not a number)
df.dropna(inplace=True) # drop all nans
app = FastAPI()

@app.get("/")
async def root():
    return {df.to_json(orient="records")}
