from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()

saturation_data = [
  (0.05, 0.00105, 30.0),
  (0.1,  0.0011, 15.0),
  (0.5,  0.0012, 3.5),
  (1.0,  0.0013, 1.9),
  (2.0,  0.00135, 1.0),
  (5.0,  0.0016, 0.3),
  (7.0,  0.0025, 0.1),
  (9.0,  0.0032, 0.004),
  (10.0, 0.0035, 0.0035),
]

def interpolate(p: float):
  p1, vf1, vg1 = saturation_data[0]
  p2, vf2, vg2 = saturation_data[1]
  factor = (p - p1) / (p2 - p1)
  vf = vf1 + factor * (vf2 - vf1)
  vg = vg1 + factor * (vg2 - vg1)
  return round(vf, 6), round(vg, 6)

@router.get("/phase-change-diagram")
def get_phase_change_diagram(pressure: float = Query(..., gt=0, lt=10.01)):
  if pressure < 0.05 or pressure > 10.0:
    return JSONResponse(
      status_code=400,
      content={"error": "Pressure must be between 0.05 and 10 MPa."}
    )
  vf, vg = interpolate(pressure)
  return {
    "specific_volume_liquid": vf,
    "specific_volume_vapor": vg
  }
