from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_root():
    return { "marks": [10, 20] }