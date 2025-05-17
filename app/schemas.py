from pydantic import BaseModel
from typing import Literal

class NotificationRequest(BaseModel):
    user_id: int
    recipient: str
    type: Literal["email", "sms", "in-app"]
    content: str
