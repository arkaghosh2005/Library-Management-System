# 📚 Library Management System

A web-based Library Management System built using Django (Python) to manage books, users, and borrowing records efficiently.

---

## 🚀 Features

- Add, update, and delete books  
- Manage users (add, edit, view)  
- Issue and return books  
- Track borrowing records (Open / Closed)  
- Dashboard for system overview  

---

## 🛠️ Tech Stack

- Backend: Django (Python)  
- Frontend: HTML, CSS  
- Database: SQLite  
- Version Control: Git & GitHub  

---

## 📂 Project Structure
management_project/
│
├── management_app/
│ ├── migrations/
│ ├── admin.py
│ ├── apps.py
│ ├── form.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── management_project/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│
├── templates/
│ ├── BookAdd.html
│ ├── BookDetails.html
│ ├── BookEdit.html
│ ├── BookTable.html
│ ├── Dashboard.html
│ ├── RecordsBorrowBook.html
│ ├── RecordsClosed.html
│ ├── RecordsOpen.html
│ ├── Sidebar.html
│ ├── UserAdd.html
│ ├── UserDetails.html
│ ├── UserEdit.html
│ ├── UserTable.html
│
├── manage.py
├── README.md


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
git clone https://github.com/arkaghosh2005/Library-Management-System.git

cd library-management-system

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install django

### 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Run Server
python manage.py runserver

---

## 🧠 Modules

### Book Management
- Add books  
- Edit books  
- View books  

### User Management
- Add users  
- Edit users  
- View users  

### Borrowing System
- Issue books  
- Track records  
- Return books  

### Dashboard
- System overview  

---

## 📌 Future Improvements

- User authentication (login/signup)  
- Responsive UI (Bootstrap)  
- Reports & analytics  
- Deployment (AWS / Render)  

---

## 🤝 Contribution

1. Fork the repository  
2. Create a new branch  
3. Make changes  
4. Submit a pull request  

---

## 📄 License

MIT License  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
