# LMS : Library Management System

<div align="center">

![LMS](https://img.shields.io/badge/LMS-Library_Management_System-646CFF?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3.14.2-339933?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.3-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.x-38B2AC?style=for-the-badge&logo=mysql&logoColor=white)

**A full-featured, responsive Library Management System built from scratch using Django and MySQL. Manage books, users, and borrowing records with automated fine calculation, stock tracking, and a clean modern UI.**

</div>

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [URL Reference](#url-reference)
- [Sponsor](#sponsor)
- [License](#license)

---

<a id="features"></a>

## ✨ Features

### 📊 Dashboard
| Feature | Description |
|---------|-------------|
| **Overview Statistics** | Real-time counts of total users, total books, borrowed books, and returned books |
| **Quick Navigation** | Central hub with links to all modules |

### 📚 Book Management
| Feature | Description |
|---------|-------------|
| **Add Books** | Register new books with name, author, type, and stock quantity |
| **Edit Books** | Update book details with automatic available stock adjustment |
| **Delete Books** | Remove books from the catalog |
| **Book Details** | View complete information for any book |
| **Book Categories** | Classify books as Fiction, Non-Fiction, Science, History, Biography, Technology, Literature, or Other |
| **Smart Stock Tracking** | Available count auto-adjusts when stock is edited (preserves issued count) |
| **Form Validation** | Server-side validation for book name, author, type, and stock |

### 👥 User Management
| Feature | Description |
|---------|-------------|
| **Add Users** | Register library members with full name, phone, email, and address |
| **Edit Users** | Update user information with duplicate email/phone prevention |
| **Delete Users** | Remove users from the system |
| **User Details** | View complete profile of any user |
| **Search & Filter** | Search users by name or email with case-insensitive matching |
| **Form Validation** | Full name (min 2 words), 10-digit phone, unique email enforcement |

### 📖 Borrowing Records
| Feature | Description |
|---------|-------------|
| **Issue Books** | Borrow a book with user selection, book selection, and due date |
| **Return Books** | Return issued books with automatic stock restoration |
| **Reissue Books** | Reissue a book from the current date with a fresh 14-day window |
| **Open Records** | View all currently issued books with search and date filtering |
| **Closed Records** | View all returned books with return date and fine history |
| **Smart User Filtering** | Only users without active borrowings appear in the issue form |
| **Available Books Only** | Only books with available stock can be issued |

### 💰 Fine System
| Feature | Description |
|---------|-------------|
| **Automatic Fine Calculation** | ₹5/day fine for overdue books, calculated in real-time |
| **Live Fine Display** | Open records show the current accumulated fine dynamically |
| **Pay & Return Button** | Red "Pay & Return" button replaces green "Return" when a fine is owed |
| **Fine on Return** | Final fine amount is locked and saved when the book is returned |

### 🎨 UI & Design
| Feature | Description |
|---------|-------------|
| **Modern Design** | Clean, professional interface with custom CSS styling |
| **Responsive Layout** | Sidebar navigation with adaptive layouts for all screen sizes |
| **Gradient Backgrounds** | Subtle radial gradients for visual depth |
| **Smooth Animations** | FadeUp animations and hover transitions throughout |
| **Google Fonts** | Manrope font family for a premium look |
| **Form Error Display** | Inline red error messages below each form field on validation failure |

---

<a id="tech-stack"></a>

## 🛠 Tech Stack

### Backend Technologies
| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.14.2 | Programming Language |
| Django | 6.0.3 | Web Framework (MVT Architecture) |
| MySQL | 8.x | Relational Database |
| mysqlclient | - | MySQL Database Connector |
| python-dotenv | - | Environment Variable Management |

### Frontend Technologies
| Technology | Purpose |
|------------|---------|
| HTML5 | Page Structure & Templates |
| CSS3 | Custom Styling (No frameworks) |
| Django Template Engine | Dynamic Content Rendering |

### Key Django Features Used
| Feature | Purpose |
|---------|---------|
| Django ORM | Database queries with Q objects for complex filtering |
| ModelForms | Form generation with custom validation |
| Template Inheritance | Reusable sidebar via `{% include %}` |
| CSRF Protection | Built-in security for all POST forms |
| Virtual Environment | Isolated Python dependencies |

---

<a id="system-architecture"></a>

## 🏗 System Architecture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                          CLIENT (Browser)                                    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌───────────┐   │
│  │ Dashboard  │ │   Books    │ │   Users    │ │  Records   │ │  Sidebar  │   │
│  │            │ │  Table     │ │  Table     │ │Open/Closed │ │Navigation │   │
│  └─────┬──────┘ └─────┬──────┘ └─────┬──────┘ └──────┬─────┘ └───────────┘   │
│        │              │              │               │                       │
│        │    ┌─────────┴────────┐     │    ┌──────────┴──────────┐            │
│        │    │ Add/Edit/Details │     │    │ Borrow/Return/      │            │
│        │    │ /Delete Book     │     │    │ Reissue Book        │            │
│        │    └──────────────────┘     │    └─────────────────────┘            │
│        │                             │                                       │
│        └──────────────┬──────────────┘                                       │
│                       │                                                      │
│              HTML Forms (POST/GET)                                           │
│                                                                              │
└───────────────────────┬──────────────────────────────────────────────────────┘
                        │
════════════════════════════════════════════════════════════════════════════════
                        │           HTTP (Port 8000)
════════════════════════════════════════════════════════════════════════════════
                        │
┌───────────────────────┴──────────────────────────────────────────────────────┐
│                     SERVER (Django 6.0.3 + Python 3.14.2)                    │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                        URL ROUTER (urls.py)                           │   │
│  │                                                                       │   │
│  │   /               → dashboard          /users/        → user_table    │   │
│  │   /books/          → book_table         /user/add/     → user_add     │   │
│  │   /book/add/       → book_add           /user/<id>/    → user_details │   │
│  │   /book/<id>/      → book_details       /user/<id>/edit/  → user_edit │   │
│  │   /book/<id>/edit/ → book_edit          /user/<id>/delete/→ user_del  │   │
│  │   /book/<id>/delete/→ book_delete                                     │   │
│  │   /records/open/   → records_open       /return/<id>/  → return_book  │   │
│  │   /records/closed/ → records_closed     /reissue/<id>/ → reissue_book │   │
│  │   /records/borrow/ → records_borrow                                   │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                        VIEWS (views.py)                               │   │
│  │                                                                       │   │
│  │  Dashboard    │ Stats aggregation (count queries)                     │   │
│  │  Book CRUD    │ Add, Edit, Delete, Details with stock management      │   │
│  │  User CRUD    │ Add, Edit, Delete, Details with search/filter         │   │
│  │  Records      │ Open/Closed records with search & date filtering      │   │
│  │  Borrow       │ Issue book + decrement available stock                │   │
│  │  Return       │ Return book + increment stock + calculate fine        │   │
│  │  Reissue      │ Reset issue_date to today + new 14-day due_date       │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                     FORMS & VALIDATION (form.py)                      │   │
│  │                                                                       │   │
│  │  userDataForm    │ Full name, phone (10-digit), unique email          │   │
│  │  bookDataForm    │ Book name, author, type, stock (non-negative)      │   │
│  │  issueBookForm   │ User, book, due date with conflict checks          │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐   │
│  │                       MODELS (models.py)                              │   │
│  │                                                                       │   │
│  │  userData       │ full_name, phone_no, email, address                 │   │
│  │  bookData       │ book_name, author_name, book_type, stock, available │   │
│  │  issueBookData  │ user(FK), book(FK), dates, fine_amount, status      │   │
│  └───────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────┬───────────────────────────────────────────┘
                                   │
                                   │ Django ORM (mysqlclient)
                                   ▼
                    ┌─────────────────────────────────────┐
                    │           MySQL Database            │
                    │            (library_db)             │
                    │                                     │
                    │  ┌───────────────────────────────┐  │
                    │  │   management_app_userdata     │  │
                    │  │  • id (PK, Auto)              │  │
                    │  │  • full_name (VARCHAR 150)    │  │
                    │  │  • phone_no (VARCHAR 15)      │  │
                    │  │  • email (VARCHAR, UNIQUE)    │  │
                    │  │  • address (TEXT, nullable)   │  │
                    │  └───────────────────────────────┘  │
                    │  ┌───────────────────────────────┐  │
                    │  │   management_app_bookdata     │  │
                    │  │  • id (PK, Auto)              │  │
                    │  │  • book_name (VARCHAR 200)    │  │
                    │  │  • author_name (VARCHAR 150)  │  │
                    │  │  • book_type (VARCHAR 20)     │  │
                    │  │  • stock (INT, default 0)     │  │
                    │  │  • available (INT, default 0) │  │
                    │  └───────────────────────────────┘  │
                    │  ┌───────────────────────────────┐  │
                    │  │ management_app_issuebookdata  │  │
                    │  │  • id (PK, Auto)              │  │
                    │  │  • user_id (FK → userdata)    │  │
                    │  │  • book_id (FK → bookdata)    │  │
                    │  │  • issue_date (DATE)          │  │
                    │  │  • due_date (DATE)            │  │
                    │  │  • return_date (DATETIME)     │  │
                    │  │  • fine_amount (FLOAT)        │  │
                    │  │  • status (VARCHAR 20)        │  │
                    │  └───────────────────────────────┘  │
                    └─────────────────────────────────────┘
```

---

<a id="database-schema"></a>

## 🗄 Database Schema

### userData
| Field | Type | Constraints |
|-------|------|-------------|
| `id` | BigAutoField | Primary Key, Auto-increment |
| `full_name` | CharField(150) | Required |
| `phone_no` | CharField(15) | Required, 10-digit, Unique |
| `email` | EmailField | Required, Unique |
| `address` | TextField | Optional, Nullable |

### bookData
| Field | Type | Constraints |
|-------|------|-------------|
| `id` | BigAutoField | Primary Key, Auto-increment |
| `book_name` | CharField(200) | Required |
| `author_name` | CharField(150) | Required |
| `book_type` | CharField(20) | Choices: Fiction, Non-Fiction, Science, History, Biography, Technology, Literature, Other |
| `stock` | PositiveIntegerField | Default: 0 |
| `available` | PositiveIntegerField | Default: 0, Auto-managed |

### issueBookData
| Field | Type | Constraints |
|-------|------|-------------|
| `id` | BigAutoField | Primary Key, Auto-increment |
| `user` | ForeignKey | → userData, CASCADE |
| `book` | ForeignKey | → bookData, CASCADE |
| `issue_date` | DateField | Auto-set on creation |
| `due_date` | DateField | Default: today + 14 days |
| `return_date` | DateTimeField | Nullable, set on return |
| `fine_amount` | FloatField | Default: 0.00 |
| `status` | CharField(20) | Choices: Issued / Returned |

---

<a id="project-structure"></a>

## 📁 Project Structure

```
management_project/
├── manage.py                              # Django management script
├── .env                                   # Environment variables (DB config)
│
├── management_project/                    # Django Project Configuration
│   ├── __init__.py
│   ├── settings.py                        # Project settings (DB, apps, middleware)
│   ├── urls.py                            # Root URL configuration
│   ├── wsgi.py                            # WSGI entry point
│   └── asgi.py                            # ASGI entry point
│
├── management_app/                        # Main Application
│   ├── __init__.py
│   ├── admin.py                           # Django admin configuration
│   ├── apps.py                            # App configuration
│   ├── models.py                          # Database models (userData, bookData, issueBookData)
│   ├── form.py                            # ModelForms with custom validators
│   ├── views.py                           # View functions (11 views)
│   ├── urls.py                            # App URL patterns (14 routes)
│   ├── tests.py                           # Test cases
│   └── migrations/                        # Database migrations
│       ├── __init__.py
│       └── 0001_initial.py                # Initial schema
│
└── templates/                             # HTML Templates
    ├── Sidebar.html                       # Reusable sidebar navigation
    ├── Dashboard.html                     # Main dashboard with stats
    ├── BookTable.html                     # Book catalog listing
    ├── BookAdd.html                       # Add new book form
    ├── BookEdit.html                      # Edit book form
    ├── BookDetails.html                   # Book detail view
    ├── UserTable.html                     # User listing with search
    ├── UserAdd.html                       # Add new user form
    ├── UserEdit.html                      # Edit user form
    ├── UserDetails.html                   # User detail view
    ├── RecordsOpen.html                   # Active borrowing records
    ├── RecordsClosed.html                 # Returned book records
    └── RecordsBorrowBook.html             # Issue book form
```

---

<a id="getting-started"></a>

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (recommended: 3.14.x)
- MySQL 8.x installed and running
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arkaghosh2005/LibraTrack.git
   cd LibraTrack
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv mylibrary
   mylibrary\Scripts\activate        # Windows
   source mylibrary/bin/activate     # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install django mysqlclient python-dotenv
   ```

4. **Create the MySQL database**
   ```sql
   CREATE DATABASE library_db;
   ```

5. **Configure environment variables** (see [Environment Variables](#environment-variables))

6. **Run database migrations**
   ```bash
   cd management_project
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and navigate to `http://127.0.0.1:8000`

---

<a id="environment-variables"></a>

## ⚙️ Environment Variables

### Project Root (`management_project/.env`)

```env
# MySQL Database Configuration
DB_NAME=library_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

<a id="url-reference"></a>

## 📚 URL Reference

### Dashboard
| Method | URL | View | Description |
|--------|-----|------|-------------|
| `GET` | `/` | `dashboard` | Main dashboard with statistics |

---

### Book Management
| Method | URL | View | Description |
|--------|-----|------|-------------|
| `GET` | `/books/` | `book_table` | List all books |
| `GET/POST` | `/book/add/` | `book_add` | Add a new book |
| `GET` | `/book/<id>/` | `book_details` | View book details |
| `GET/POST` | `/book/<id>/edit/` | `book_edit` | Edit a book |
| `GET` | `/book/<id>/delete/` | `book_delete` | Delete a book |

---

### User Management
| Method | URL | View | Description |
|--------|-----|------|-------------|
| `GET` | `/users/` | `user_table` | List all users (with search) |
| `GET/POST` | `/user/add/` | `user_add` | Register a new user |
| `GET` | `/user/<id>/` | `user_details` | View user profile |
| `GET/POST` | `/user/<id>/edit/` | `user_edit` | Edit user info |
| `GET` | `/user/<id>/delete/` | `user_delete` | Delete a user |

---

### Records & Transactions
| Method | URL | View | Description |
|--------|-----|------|-------------|
| `GET` | `/records/open/` | `records_open` | Active borrowing records |
| `GET` | `/records/closed/` | `records_closed` | Returned book records |
| `GET/POST` | `/records/borrow/` | `records_borrow` | Issue a book to a user |
| `GET` | `/return/<id>/` | `return_book` | Return a book (+ fine calc) |
| `GET` | `/reissue/<id>/` | `reissue_book` | Reissue from today + 14 days |

---

<a id="sponsor"></a>

## 💖 Sponsor

If you find **Library Management System** helpful and would like to support its continued development, consider sponsoring!

<div align="center">

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor%20on-GitHub-ea4aaa?style=for-the-badge&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/arkaghosh2005)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A-Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=white)](https://buymeacoffee.com/arkaghosh2005)

</div>

Your support helps cover hosting development time and enables new features. Every contribution is greatly appreciated! ☕✨

---

<a id="license"></a>

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by **Arka Ghosh, Arpan Paul, Ankita Roy and Anirban Mehata**

</div>