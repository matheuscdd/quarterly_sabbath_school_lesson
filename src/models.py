import json
import requests as req
from pydantic import BaseModel, HttpUrl, EmailStr, validator, ValidationError


class Body(BaseModel):
    email: EmailStr
    url: HttpUrl

    def url_exists(cls, val):
        error = json.dumps(
            [
                {
                    "ctx": {"error": "relative URL not found"},
                    "input": val,
                    "loc": ["url"],
                    "msg": "Input should be a valid and existing URL",
                    "type": "url_check",
                }
            ]
        )
        try:
            response = req.get(val)
            if response.status_code != 200:
                raise ValueError(error)
        except req.exceptions.RequestException as e:
            raise ValueError(error)
