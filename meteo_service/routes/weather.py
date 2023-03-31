from fastapi import APIRouter, Depends

from meteo_service.dependencies import meteo_service_dependency
from meteo_service.integrations.open_meteo_api import Probe
from meteo_service.services.meteo_service import MeteoService

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/weather/{city}", response_model=list[Probe])
async def get_weather(
    city: str, meteo_service: MeteoService = Depends(meteo_service_dependency)
) -> list[Probe]:
    return await meteo_service(city)
