# 📚 Library Management System

A simple desktop GUI application built using **PySide6** and **MySQL**, designed to manage books in a library database. This tool allows users to add, remove, and view books using a clean interface.

---

## 🚀 Features

- ✅ Add books with title, author, and year  
- 🗑️ Remove books by ID  
- 👀 Display all books in a message box  
- 💾 MySQL integration for persistent storage  
- 🎨 PySide6 GUI with styled buttons

---

## 🛠️ Tech Stack

- Python 3  
- PySide6  
- MySQL  
- mysql-connector-python

---

## 📦 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/utk1college/LibraryManagementSystem.git
cd LibraryManagementSystem
```

### 2. Install Requirements

```bash
pip install PySide6 mysql-connector-python
```

### 3. Setup MySQL Database

Login to MySQL and run:

```sql
CREATE DATABASE library_db;

USE library_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    year INT
);
```

Make sure to update your MySQL credentials in `library_app.py` if needed.

---

## ▶️ How to Run

```bash
python library_app.py
```

---

## 📝 File Structure

```
LibraryManagementSystem/
├── library_app.py
└── README.md
```

---

## 💡 Future Features (Planned)

* Add icons to buttons  
* Search by title/author  
* Update/edit book entries  
* Export book list to CSV/PDF  
* User login system  
* SQLite option for portability

---

## 🙋‍♂️ Author

**Utkrisht Umang**  
* GitHub: [utk1college](https://github.com/utk1college)  
* Email: [utkrisht.works@gmail.com](mailto:utkrisht.works@gmail.com)

---
