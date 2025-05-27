# 💬 Django Channels Chat App

This is a real-time chat application built using **Django**, **Django Channels**, and **WebSockets**. Users can join a chat room, enter a username, and exchange messages in real-time — all without reloading the page.

---

## 🚀 Features

- Real-time messaging with WebSockets
- Join rooms by URL (e.g. `/chat/testroom/`)
- Enter your name before sending messages
- Simple and clean UI with auto-scrolling
- Built with Django Channels and ASGI

---

## 📦 Requirements

- Python 3.7+
- Django 4.x
- Channels
- ASGI server (e.g. Daphne or Uvicorn)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-channels-chat.git
cd django-channels-chat
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install django channels daphne
python manage.py migrate
daphne chat_project.asgi:application
uvicorn chat_project.asgi:application --reload
http://127.0.0.1:8000/chat/testroom/
chat_project/
│
├── chat/
│   ├── templates/
│   │   └── chatroom.html
│   ├── consumers.py
│   ├── routing.py
│   └── views.py
│
├── chat_project/
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
