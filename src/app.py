# Install Dependencies
from fastapi import FastAPI
import  uvicorn

app = FastAPI()

@app.get("/addition")
def calculation_addition(a: int,b: int):
    if (a+b) % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
    
@app.get("/multiplication")
def calculation_mul(a: int,b: int):
    if (a*b) % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000)