from pydantic import BaseModel
from typing import List

class LoginPostRequestBody(BaseModel):
    """Request body for login endpoint."""
    username: str
    password: str
    
class LoginPostResponseBody(BaseModel):
    """Response body for login endpoint."""
    success: bool
    session_token: str
    
class FirmwareQueueGetResponseBody(BaseModel):
    """Response body for firmware queue GET endpoint."""
    queue: List[str]
    
class FirmwareGetResponseBody(BaseModel):
    """Response body for firmware GET endpoint."""
    firmware: bytes
