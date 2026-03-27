# 🌐 Bengalium (Blog Website)

A full-featured blog web application built with **Django**, where users can create, manage, and interact with blog posts. This project includes authentication, comments, likes, and an admin dashboard.

---

## 🚀 Features

### 🔐 User Authentication

- User registration and login system
- Secure logout functionality
- Only authenticated users can create, edit, or delete posts

---

### ✍️ Blog Post Management

- Create, edit, and delete blog posts
- Each post includes:
  - Title
  - Content
  - Author
  - Created date

---

### 💬 Comment System

- Users can add comments to posts
- Comments are displayed under each post

---

### ❤️ Like Feature

- Users can like and unlike posts
- Each post displays total likes

---

### 🛠 Admin Panel

- Manage users, posts, comments, and likes via Django Admin
- Admin can view, edit, and delete content

---

### 🎨 Frontend Interface

- Homepage displays all blog posts
- Individual post detail pages
- Clean and simple UI for easy navigation

---

## 🧑‍💻 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS (Bootstrap optional)
- **Database:** SQLite

---

## ⚙️ Installation & Setup

# 1. Clone the repository

```bash
git clone https://github.com/MdNasif2000/bengalium.git
```

# 2. Navigate into the project

```bash
cd bengalium
```

# 3. Create virtual environment

```bash
python -m venv venv
```

# 4. Activate virtual environment

# Windows

```bash
venv\Scripts\activate
```

# Mac/Linux

```bash
source venv/bin/activate
```

# 5. Install dependencies

```bash
pip install -r requirements.txt
```

# 6. Run migrations

```bash
python manage.py migrations
python manage.py migrate
```

# 7. Create superuser

```bash
python manage.py createsuperuser
```

# 8. Run server

```bash
python manage.py runserver
```

---

# 🔑 Admin Access

```bash
http://127.0.0.1:8000/admin/
```
