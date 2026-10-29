from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"message": "API healthy"}
