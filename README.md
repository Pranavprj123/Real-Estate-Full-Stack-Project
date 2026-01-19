# 🏠 RealEstate – Property Listing & Visit Management System

A full-stack Django web application that allows users to browse properties, request visits, and track booking status, while admins manage properties and approvals.

---

## 🚀 Features

### 👥 Users
- Browse properties without login
- View property details with image gallery
- Book visit (login required)
- Track visit status (Pending / Approved / Rejected)
- Dashboard to view visit history

### 🛠 Admin
- Add / Edit / Delete properties
- Upload multiple images per property
- View all visit requests
- Approve / Reject visit requests

---

## 🧰 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Authentication:** Django Auth
- **Media Handling:** Django Media Files
- **UI:** Responsive, modern design

---

## 📂 Project Structure

- `accounts` – Authentication & user dashboard
- `properties` – Property listing & details
- `visits` – Visit booking & approval
- `templates` – HTML templates
- `media` – Uploaded images

---

## ⚙️ How to Run Locally

```bash
git clone <repo-url>
cd realestate
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
