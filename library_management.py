import mysql.connector as mysql
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QInputDialog, QMessageBox
from PySide6.QtGui import QIcon
import sys

# Database connection setup
def connect_to_db():
    return mysql.connect(
        host='localhost',
        user='root',
        password='database001!',
        database='library_db'
    )

# Add Book
def add_book():
    title, ok1 = QInputDialog.getText(window, 'Input', 'Enter book title:')
    author, ok2 = QInputDialog.getText(window, 'Input', 'Enter author name:')
    year, ok3 = QInputDialog.getInt(window, 'Input', 'Enter publication year:')

    if ok1 and ok2 and ok3:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
            cursor.execute(query, (title, author, year))
            conn.commit()
            conn.close()
            QMessageBox.information(window, "Success", "Book added successfully!")
        except mysql.Error as err:
            QMessageBox.critical(window, "Database Error", f"An error occurred: {err}")
    else:
        QMessageBox.warning(window, "Warning", "All fields are required!")

# Remove Book
def remove_book():
    book_id, ok = QInputDialog.getInt(window, 'Input', 'Enter ID of the book to remove:')

    if ok and book_id:
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            query = "DELETE FROM books WHERE id = %s"
            cursor.execute(query, (book_id,))
            conn.commit()
            conn.close()
            QMessageBox.information(window, "Success", "Book removed successfully!")
        except mysql.Error as err:
            QMessageBox.critical(window, "Database Error", f"An error occurred: {err}")
    else:
        QMessageBox.warning(window, "Warning", "Book ID is required!")

# Display Books
def display_books():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT * FROM books"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()

        result = ""
        for row in rows:
            result += f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}\n"

        if result:
            QMessageBox.information(window, "Book List", result)
        else:
            QMessageBox.information(window, "Book List", "No books found!")
    except mysql.Error as err:
        QMessageBox.critical(window, "Database Error", f"An error occurred: {err}")

# Main GUI Setup
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Library Management System")
window.setGeometry(100, 100, 400, 300)

layout = QVBoxLayout()
window.setLayout(layout)

# Buttons with Icons and Styles
btn_add = QPushButton("Add Book")
btn_add.setIcon(QIcon('icons/add.png'))  # Ensure the path is correct
btn_add.setStyleSheet("background-color: #4CAF50; color: white;")

btn_remove = QPushButton("Remove Book")
btn_remove.setIcon(QIcon('icons/remove.png'))  # Ensure the path is correct
btn_remove.setStyleSheet("background-color: #f44336; color: white;")

btn_display = QPushButton("Display Books")
btn_display.setIcon(QIcon('icons/display.png'))  # Ensure the path is correct
btn_display.setStyleSheet("background-color: #2196F3; color: white;")

# Add only required buttons to the layout
layout.addWidget(btn_add)
layout.addWidget(btn_remove)
layout.addWidget(btn_display)

# Connect buttons to their functions
btn_add.clicked.connect(add_book)
btn_remove.clicked.connect(remove_book)
btn_display.clicked.connect(display_books)

window.show()
sys.exit(app.exec())
