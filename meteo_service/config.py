from pydantic import BaseSettings


class Config(BaseSettings):
    open_meteo_api: str = "https://api.open-meteo.com/v1/forecast"

    login: str = "admin"
    password: str = "admin"
    host: str = "postgres"
    port: str = "5432"
    database: str = "db1"


config = Config()
