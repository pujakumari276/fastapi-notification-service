from fastapi import APIRouter
from app.schemas import NotificationRequest
from app import services

router = APIRouter()

@router.post("/notifications")
def send_notification(payload: NotificationRequest):
    return services.send_notification(payload)

@router.get("/users/{user_id}/notifications")
def get_user_notifications(user_id: int):
    return services.get_notifications_for_user(user_id)



