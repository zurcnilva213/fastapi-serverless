from datetime import datetime

from mangum import Mangum
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from core.settings import Settings
from src import auth, company, podium, crm, booking


class AppMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, req: Request, call_next):
        if (
                not req.session.get('is_authenticated')
                and 'static' not in req.url.path
                and 'api' not in req.url.path
                and 'ping' not in req.url.path
        ):
            return RedirectResponse(f'{req.app.settings.app_root_path}/apidocs')

        # process the request and get the response
        response = await call_next(req)
        return response


settings = Settings()
app = FastAPI(
    version=settings.app_version,
    title=settings.app_title,
    docs_url=settings.app_docs_url,
    openapi_url=settings.app_openapi_url,
    root_path=settings.app_root_path,
    dependencies=[]
)
app.settings = settings
app.add_middleware(AppMiddleware)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.app_secret
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/ping', include_in_schema=False)
async def index():
    return {'pong': datetime.utcnow().isoformat()}

app.include_router(auth.router, prefix=settings.api_router_prefix)
app.include_router(company.router, prefix=settings.api_router_prefix)
app.include_router(podium.router, prefix=settings.api_router_prefix)
app.include_router(crm.router, prefix=settings.api_router_prefix)
app.include_router(crm.router_without_auth, prefix=settings.api_router_prefix)
app.include_router(booking.router, prefix=settings.api_router_prefix)


# MANGUM-------------------
handler = Mangum(app=app)
# -------------------------
