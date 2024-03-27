import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    company: str = os.getenv("COMPANY")
    app_version: str = os.getenv("APP_VERSION", "0.0.1")
    app_root_path: str = os.getenv("APP_ROOT_PATH", "")
    app_title: str = os.getenv("APP_TITLE", "Fulcrum API")
    app_docs_url: str = os.getenv("APP_DOC_URL", "/apidocs")
    app_openapi_url: str = os.getenv("APP_OPENAPI_PATH", "/openapi.json")
    app_secret: str = os.getenv("APP_SECRET", "")
    api_router_prefix: str = os.getenv("APP_API_PREFIX", "/api/v1")

    cred_username: str = os.getenv("CRED_USERNAME", "fulcrum_admin")
    cred_password: str = os.getenv("CRED_PASSWORD", "")

    min_connection: int = os.getenv("MIN_CONNECTION")
    max_connection: int = os.getenv("MAX_CONNECTION")

    database_host: str = os.getenv("DB_HOST", "")
    database_port: str = os.getenv("DB_PORT", "")
    database_user: str = os.getenv("DB_USER", "")
    database_pass: str = os.getenv("DB_PASS", "")
    database_url: str = os.getenv("DB_URL", "")
    database_name: str = os.getenv("DB_NAME", "")

    adlev_database_host: str = os.getenv("ADLEV_DB_HOST", "")
    adlev_database_port: str = os.getenv("ADLEV_DB_PORT", "")
    adlev_database_user: str = os.getenv("ADLEV_DB_USER", "")
    adlev_database_pass: str = os.getenv("ADLEV_DB_PASS", "")
    adlev_database_url: str = os.getenv("ADLEV_DB_URL", "")
    adlev_database_name: str = os.getenv("ADLEV_DB_NAME", "")

    datacube_api_url: str = os.getenv("DATACUBE_API_URL")
    datacube_api_user: str = os.getenv("DATACUBE_API_USER")
    datacube_api_pass: str = os.getenv("DATACUBE_API_PASS")

    database_url_auth: str = os.getenv("DB_URL_AUTH", "")
    database_name_auth: str = os.getenv("DB_NAME_AUTH", "")


    app_host: str = os.getenv("APP_HOST", "")
    podium_client_id: str = os.getenv("PODIUM_CLIENT_ID", "")
    podium_client_secret: str = os.getenv("PODIUM_CLIENT_SECRETE", "")

    page_size: int = 25
    cors_origins: list = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://0.0.0.0:3000",
        "http://bookingadminwebapp.s3-website.us-east-2.amazonaws.com",
        "https://bookingadminwebapp.s3-website.us-east-2.amazonaws.com",
        "https://be7wgaoisxjac7qqti2serjquy0rsgwt.lambda-url.us-east-2.on.aws",
        "*"
    ]

    timer_watch_threshold: float = float(os.getenv("TIMER_WATCH_THRESHOLD", 1))
