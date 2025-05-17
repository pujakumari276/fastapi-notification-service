# Fake in-memory storage
notification_db = []

def send_notification(payload):
    # Simulate sending
    print(f"Sending {payload.type} to {payload.recipient}: {payload.content}")
    # Save to "DB"
    notification_db.append({
        "user_id": payload.user_id,
        "type": payload.type,
        "recipient": payload.recipient,
        "content": payload.content
    })
    return {"message": f"{payload.type} sent successfully"}

def get_notifications_for_user(user_id):
    user_notifications = [n for n in notification_db if n["user_id"] == user_id]
    return {"user_id": user_id, "notifications": user_notifications}
