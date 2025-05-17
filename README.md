Notification Service

Objective
Build a system to send notifications to users via Email, SMS, and In-App.

API Endpoints
- POST /notifications: Send a notification
- GET /users/{id}/notifications: Get all notifications for a user

Setup Instructions
1. Clone this repo
2. Create virtual environment:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run the server:
uvicorn main:app --reload
4. Visit Swagger UI for testing:
- http://127.0.0.1:8000/docs

Assumptions
- No real email/SMS sending – only console logging
- Notifications stored in-memory for simplicity


