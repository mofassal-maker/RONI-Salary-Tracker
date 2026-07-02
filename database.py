import sqlite3
import os

DB_NAME = "data/salary.db"

os.makedirs("data", exist_ok=True)


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Salary Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS salary(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        month TEXT NOT NULL
    )
    """)

    # Expense Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        reason TEXT NOT NULL,
        category TEXT NOT NULL,
        expense_date TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_salary(amount, month):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM salary WHERE month=?", (month,))
    cur.execute(
        "INSERT INTO salary(amount, month) VALUES(?, ?)",
        (amount, month)
    )

    conn.commit()
    conn.close()


def get_salary(month):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT amount FROM salary WHERE month=?",
        (month,)
    )

    row = cur.fetchone()

    conn.close()

    return row[0] if row else 0


def add_expense(amount, reason, category, expense_date):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO expenses(amount, reason, category, expense_date)
    VALUES (?, ?, ?, ?)
    """, (amount, reason, category, expense_date))

    conn.commit()
    conn.close()


def get_total_expense():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT SUM(amount) FROM expenses")

    total = cur.fetchone()[0]

    conn.close()

    return total if total else 0


def get_all_expenses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT id, expense_date, reason, category, amount
    FROM expenses
    ORDER BY expense_date DESC, id DESC
    """)

    data = cur.fetchall()

    conn.close()

    return data


def delete_expense(expense_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    conn.commit()
    conn.close()


def export_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT expense_date, reason, category, amount
    FROM expenses
    ORDER BY expense_date DESC
    """)

    data = cur.fetchall()

    conn.close()

    return data