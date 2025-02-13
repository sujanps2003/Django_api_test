# Django API Testing

## 📌 Overview

This project implements a **Django REST API** for managing **Users, Patients, and Heart Rate data**. It provides separate endpoints for retrieving and creating patient and heart rate records using `ListCreateAPIView`.

---

## 🚀 Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** SQLite (default, but can be changed to PostgreSQL)
- **Tools:** Postman/cURL for API testing

---

## 🛠️ Setup Instructions

### **1️⃣ Clone the Repository**

```sh
git clone <https://github.com/sujanps2003/Django_api_test.git>
cd backend_api
```

### **2️⃣ Create a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**

```sh
pip install django djangorestframework
```

### **4️⃣ Apply Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Run the Server**

```sh
python manage.py runserver
```

The API will be available at: **`http://127.0.0.1:8000/`**

---

## 📜 Assumptions & Decisions

1. **No authentication required** (as per instructions).
2. **Separate endpoints** for `list` and `create` actions for both Patients and Heart Rate records.
3. **Passwords are stored securely** using Django’s `make_password()`.
4. **SQLite is used as the default database**, but can be replaced with PostgreSQL/MySQL.

---

## 📌 API Documentation

### **1️⃣ User API**

| Method | Endpoint         | Description                 |
| ------ | ---------------- | --------------------------- |
| `POST` | `/api/register/` | Register a new user         |
| `POST` | `/api/login/`    | Login with email & password |

#### **Example: Register User**

```sh
curl -X POST http://127.0.0.1:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "securepassword"}'
```

---

### **2️⃣ Patient API**

| Method | Endpoint                | Description           |
| ------ | ----------------------- | --------------------- |
| `POST` | `/api/patients_create/` | Add a new patient     |
| `GET`  | `/api/patients_list/`   | Retrieve all patients |

#### **Example: Retrieve All Patients**

```sh
curl -X GET http://127.0.0.1:8000/api/patients_list/
```

---

### **3️⃣ Heart Rate API**

| Method | Endpoint                  | Description                     |
| ------ | ------------------------- | ------------------------------- |
| `POST` | `/api/heart_rate_create/` | Record a heart rate measurement |
| `GET`  | `/api/heart_rate_list/`   | Retrieve all heart rate records |

#### **Example: Create Heart Rate Record**

```sh
curl -X POST http://127.0.0.1:8000/api/heart_rate_create/ \
     -H "Content-Type: application/json" \
     -d '{"patient": 1, "bpm": 75}'
```

---

## 🛠️ Testing with Postman

1. **Open Postman** and create a new request.
2. **Set the request type** (e.g., `POST` or `GET`).
3. **Enter the API endpoint** (e.g., `http://127.0.0.1:8000/api/patients_create/`).
4. **For `POST` requests**, go to the **Body** tab and select `raw` -> `JSON`, then enter the payload:
   ```json
   {
     "name": "John Doe",
     "age": 30,
     "created_by": 1
   }
   ```
5. Click **Send** and verify the response.

---

## 🎯 Final Thoughts

This project implements a **scalable backend system** for managing Users, Patients, and Heart Rate data using Django. It follows **REST API best practices** and can be extended for real-world medical applications.
