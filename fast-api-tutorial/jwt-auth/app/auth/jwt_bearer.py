


from fastapi import Request , HTTPException
from fastapi.security import HTTPBearer , HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT




class jwt_bearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwt_bearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request : Request):
        credintials : HTTPAuthorizationCredentials = await super(
                jwt_bearer, self
            ).__call__(request)    
        if credintials:
            if not credintials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme"
                )
            return credintials.credentials
        else:
            raise HTTPException(
                    status_code=403, detail="Invalid credintials"
                )
    
    def validate_token(self, token: str):
        isTokenValid : bool = False
        payload  = decodeJWT(token)
        if payload:
            isTokenValid = True
        return isTokenValid