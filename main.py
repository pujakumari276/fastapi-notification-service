from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

notifications = {}

class Notification(BaseModel):
    user_id: int
    type: str
    message: str

@app.post("/notifications")
def send_notification(notification: Notification):
    user_id = notification.user_id
    if user_id not in notifications:
        notifications[user_id] = []
    notifications[user_id].append({
        "type": notification.type,
        "message": notification.message
    })
    return {"message": "Notification sent"}

@app.get("/users/{user_id}/notifications")
def get_user_notifications(user_id: int):
    return {
        "user_id": user_id,
        "notifications": notifications.get(user_id, [])
    }
