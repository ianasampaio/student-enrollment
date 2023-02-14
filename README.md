 # Student enrollment system

A simple CRUD application with Django using Class-Based Views (CBV). It consists of a student registration system to create, update, remove, search and list students.

## 🚀 Getting Started

---

Follow the steps to install the project on your local machine.

### 📋 Prerequisites

You need the following elements to use the service:

```
Docker
docker-compose
```

### 🔧 Installation

---

Clone this repo or download to your local machine:

```sh
https://github.com/ianasampaio/student-enrollment.git
```

### 📌 Usage

---

In your project root run:

```
docker-compose up --build
```
To migrate the database:
```
docker-compose run web python manage.py migrate
```

## 🛠️ Built with

---

* [Django](https://www.djangoproject.com/)
* [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) 
* [Bootstrap 5](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
* [Docker](https://www.docker.com/)
