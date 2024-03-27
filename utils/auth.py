from fastapi import HTTPException
from fastapi.security import HTTPBearer
from datetime import datetime, timedelta
from passlib.hash import pbkdf2_sha512
import uuid
import jwt
import os


class Auth:
    """
    Utility class for authentication and authorization
    """

    security = HTTPBearer()
    secret = os.environ["SECRET"]
    expiration = timedelta(days=14)

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        return pbkdf2_sha512.verify(password, hashed_password)

    def encode_sso_token(self, user_id: uuid.UUID, user_name: str, email: str, is_admin: str, token: str) -> str:
        user_id = str(user_id)

        payload = {
            "exp": datetime.utcnow() + self.expiration,
            "user_id": user_id,
            "user": user_name,
            "email": email,
            "is_admin": is_admin,
            "token": token,
        }

        return jwt.encode(payload, self.secret, algorithm="HS256")

    def encode_token(self, user_id: uuid.UUID) -> str:
        user_id = str(user_id)
        payload = {"exp": datetime.utcnow() + self.expiration, "user_id": user_id}

        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token: str) -> dict:
        try:
            decoded = jwt.decode(token, self.secret, algorithms=["HS256"])
            decoded["user_id"] = decoded["user_id"]
            return decoded
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")


auth = Auth()
