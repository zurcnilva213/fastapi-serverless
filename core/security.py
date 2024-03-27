import secrets
from fastapi import Request, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()


def get_loggedin_user(
    req: Request, credential: HTTPBasicCredentials = Depends(security)
):
    correct_username = secrets.compare_digest(
        credential.username, req.app.settings.cred_username
    )
    correct_password = secrets.compare_digest(
        credential.password, req.app.settings.cred_password
    )
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or password is incorrect",
        )
    return credential.username
