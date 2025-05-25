# 📚 Library Management API

A RESTful API for managing a simple library system built with Django REST Framework (DRF). The API includes JWT authentication, CRUD operations for books, authors, and categories, and borrow record tracking. Swagger documentation is included for easy API exploration.

## 🚀 Features
- ✅ JWT-based Authentication (`djangorestframework-simplejwt`)
- ✅ CRUD operations for:
  - Authors
  - Categories
  - Books
  - Borrow Records
- ✅ Custom permissions (`IsAdminOrReadOnly`)
- ✅ Swagger UI for API documentation using `drf_yasg`

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/library-api.git
cd library-api
````

### 2. Create Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (optional)

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

## 🔐 Authentication (JWT)

This API uses **JWT (JSON Web Token)** for secure authentication.

### 🔑 Get JWT Token

**POST** `/api/v1/auth/jwt/create/`

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### 🔄 Refresh JWT Token

**POST** `/api/v1/auth/jwt/refresh/`

## 📁 API Endpoints

| Endpoint                      | Description                                  |
| ----------------------------  | -------------------------------------------- |
| `/api/v1/books/`              | List, Create, Retrieve, Update, Delete books |
| `/api/v1/authors/`            | CRUD for authors                             |
| `/api/v1/categories/`         | CRUD for categories                          |
| `/api/v1/borrow/`             | Borrow record operations                     |
| `/api/v1/auth/jwt/create/`    | Obtain JWT access and refresh token          |
| `/api/v1/auth/jwt/refresh/`   | Refresh JWT access token                     |

> 🔐 Endpoints are protected — provide JWT token via `Authorization: Bearer <your_token>`

## 📘 Swagger Documentation

Explore the full API using Swagger UI:

```
http://localhost:8000/swagger/
```

This includes request/response samples and detailed endpoint descriptions.

## 🧩 Models Overview

### 📗 Author

* `name`: CharField
* `biography`: TextField

### 📙 Category

* `name`: CharField
* `description`: TextField

### 📘 Book

* `title`: CharField
* `author`: FK → Author
* `category`: FK → Category
* `ISBN`: Unique CharField
* `availability`: Boolean
* `created_at`, `updated_at`: Auto timestamps

### 📕 BorrowRecord

* `member`: FK → Custom `User`
* `book`: FK → Book
* `borrow_date`, `due_date`: DateFields

## 📄 Example Request

### 🔍 Borrow Record (GET)

```http
GET /api/v1/borrow/
Authorization: Bearer <your_token>
```

### 📥 Book (POST)

```http
POST /api/v1/books/
Authorization: Bearer <admin_token>
Content-Type: application/json

{
  "title": "Django Deep Dive",
  "author": 1,
  "category": 2,
  "ISBN": "978-1234567890",
  "availability": true
}
```

## 🧰 Technologies Used

* Python 3.x
* Django 4.x
* Django REST Framework
* djangorestframework-simplejwt
* drf-yasg (Swagger)
* postgreySQL

## 📬 Contact

Made with ❤️ by \[Md Mehedi Hasan]
📧 [mdmehedihasanroby@gmail.com](mailto:mdmehedihasanroby@gmail.com)

## ✅ License

This project is licensed under the MIT License.

