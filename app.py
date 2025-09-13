from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Request received")
    return {"message": "Hello from Azure Web App + ACR!"}
