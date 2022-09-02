from pydantic import BaseSettings


class AppSettings(BaseSettings):
    app_name: str = "Test BPP"
    app_version: str = "v 0.0.1"
    api_version:str = "/api/v1"
    app_description: str = "A Demo App Provides the Implementation of BPP (Beckn Protocol Provider)"
    secret_key: str = "BPP"

class MongoSettings(BaseSettings):
    ...


class Settings(AppSettings, MongoSettings):
    ...

settings = Settings()