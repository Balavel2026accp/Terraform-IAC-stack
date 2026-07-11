from fastapi import FastAPI
from fastapi.responses import JSONResponse 
import uvicorn 
import requests
from pydantic import BaseModel
import json
from fastapi.responses import HTMLResponse
## file and class import statements

from services.CPU import CPUChecks
processors = CPUChecks()

Application = FastAPI()

@Application.get("/CPU", response_class=HTMLResponse)
def send_html():
   return processors.render_html()