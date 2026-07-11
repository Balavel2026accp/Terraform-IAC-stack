from fastapi import FastAPI
from fastapi.responses import JSONResponse 
import uvicorn 
import requests
from pydantic import BaseModel
import json
## file and class import statements

from services.CPU import CPUChecks
processors = CPUChecks()

Application = FastAPI()

@Application.get("/CPU")
def send_html():
   print(processors.render_html)