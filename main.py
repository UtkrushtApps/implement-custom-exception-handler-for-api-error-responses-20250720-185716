from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from fastapi.openapi.models import Response as OpenAPIResponse
from fastapi.openapi.utils import get_openapi

app = FastAPI()
auth_scheme = HTTPBearer()

class ErrorResponseModel:
    def __init__(self, detail: str):
        self.detail = detail

    def dict(self):
        return {"detail": self.detail}

@app.exception_handler(HTTPException)
def custom_http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    if not credentials or credentials.credentials != "secret-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing authentication token"
        )
    return {"username": "user1"}

@app.get(
    "/users/me",
    summary="Get current user info",
    responses={
        401: {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {"detail": "Invalid or missing authentication token"}
                }
            }
        },
        200: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {"username": "user1"}
                }
            }
        }
    },
)
def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

# Optionally: ensure OpenAPI response docs reflect error structure

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom Auth Error Example API",
        version="1.0.0",
        description="API with custom structured 401 error responses",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
