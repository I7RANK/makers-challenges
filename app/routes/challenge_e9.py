from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()

saturation_data = [
  (0.05, 0.00105, 30.0),
  (10.0, 0.0035, 0.0035),
]

def interpolate(p: float):
  for i in range(len(saturation_data) - 1):
    p1, vf1, vg1 = saturation_data[i]
    p2, vf2, vg2 = saturation_data[i + 1]

    if p1 <= p <= p2:
      factor = (p - p1) / (p2 - p1)
      vf = vf1 + factor * (vf2 - vf1)
      vg = vg1 + factor * (vg2 - vg1)
      return round(vf, 6), round(vg, 6)

  return None, None

@router.get("/phase-change-diagram")
def get_phase_change_diagram(pressure: float = Query(..., gt=0)):
  vf, vg = interpolate(pressure)

  if vf is None:
    return JSONResponse(
      content={"error": "Pressure out of range. Must be between 0.05 and 10 MPa."},
      status_code=400
    )

  return {
    "specific_volume_liquid": vf,
    "specific_volume_vapor": vg
  }
