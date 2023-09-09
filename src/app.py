from fastapi import FastAPI
import  uvicorn

app = FastAPI()

@app.get("/")
def calculation(a: int,b: int):
    if (a+b) % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000)