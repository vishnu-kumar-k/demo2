from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Request received")
    return {"message": "Hello from Azure Web App + ACR! We are updating the code. This should be printed. This also please work"}
