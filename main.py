from fastapi import FastAPI
from fastapi.responses import Response, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/htmls", StaticFiles(directory="htmls"), name="htmls")

@app.get('/')
def index():
    with open("htmls/index.html", "r", encoding="utf-8") as f:
        resp=f.read()
    return HTMLResponse(content=resp)