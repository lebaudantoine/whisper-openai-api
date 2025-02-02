from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from utils.config import API_KEY
from utils.exceptions import InvalidAuthenticationSchemeException, InvalidAPIKeyException


auth_scheme = HTTPBearer(scheme_name="API key")

if not API_KEY:

    def check_api_key():
        # if No API key is set, so we don't check for it.
        pass

else:

    def check_api_key(api_key: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)]):
        if api_key.scheme != "Bearer":
            raise InvalidAuthenticationSchemeException()
        if api_key.credentials != API_KEY:
            raise InvalidAPIKeyException()

        return api_key.credentials