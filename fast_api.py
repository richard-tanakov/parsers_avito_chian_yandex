from fastapi import FastAPI, Body
from fastapi.responses import FileResponse
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("index.html")
 
@app.post("/hello")
def hello(url = Body(embed=True)):
    return {"message": f"{url} Добавлен" }