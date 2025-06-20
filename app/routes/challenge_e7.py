from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse, HTMLResponse
import random

router = APIRouter()

SYSTEM_CODES = {
  "navigation": "NAV-01",
  "communications": "COM-02",
  "life_support": "LIFE-03",
  "engines": "ENG-04",
  "deflector_shield": "SHLD-05"
}

damaged_system = {"value": random.choice(list(SYSTEM_CODES.keys()))}

@router.get("/status")
def get_status():
  damaged_system["value"] = random.choice(list(SYSTEM_CODES.keys()))
  return JSONResponse(content={"damaged_system": damaged_system["value"]})

@router.get("/repair-bay")
def get_repair_bay():
  system = damaged_system["value"]
  code = SYSTEM_CODES.get(system, "UNKNOWN")
  html = f"""
  <!DOCTYPE html>
  <html>
  <head><title>Repair</title></head>
  <body>
      <div class="anchor-point">{code}</div>
  </body>
  </html>
  """
  return HTMLResponse(content=html)

@router.post("/teapot")
def teapot():
  return Response(content="I'm a teapot", status_code=418)
