from fastapi import HTTPException

class HTTPException500(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=500, detail=detail)
