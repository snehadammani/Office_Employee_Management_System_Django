# Office Employee Management System (Django)

## Project Overview
The Office Employee Management System is a Django-based web application designed to manage employee information within an organization. It allows users to add, view, filter, and remove employee records while maintaining proper relationships between employees, departments, and roles using a relational database.

---

## Features
- Add new employees with department and role assignment
- View all employees
- Filter employees based on name, department, or role
- Remove employees from the system
- Admin panel for managing departments, roles, and employees
- Foreign key relationships to ensure data integrity

---

## Tech Stack
- Backend: Django (Python)
- Frontend: HTML, Bootstrap
- Database: SQLite
- ORM: Django ORM
- Version Control: Git and GitHub

---

## Project Structure
Office_Employee_Management_System_Django/
├── employee_app/
│ ├── migrations/
│ ├── templates/
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
├── office_emp_proj/
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ ├── asgi.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md



---

## Database Design
- Department
- Role
- Employees (with foreign key relationships to Department and Role)

---

## Installation and Setup
```bash
git clone https://github.com/snehadammani/Office_Employee_Management_System_Django.git
cd Office_Employee_Management_System_Django
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Usage

Access admin panel to create departments and roles

Add employees using the web interface

View, filter, and remove employee records

Learning Outcomes

Django models and ORM

Foreign key relationships

CRUD operations

Form handling with GET and POST

Git and GitHub usage

