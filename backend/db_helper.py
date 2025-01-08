# CRUD
# C - Create
# R - Retrieve
# U - Update
# D - Delete

import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    if connection.is_connected():
        print("Connection Successful.")
    else:
        print("Failed in Connecting to a database.")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

# with get_db_cursor() as cursor:
#     print("Context manager invoked, database connection opened.")

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")

    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expense_manager.expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def insert_expenses(expense_date, amount, category, notes):
    logger.info(f"insert_expenses called with date: {expense_date}, amount: {amount}, category: {category},notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s,  %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    '''
    SELECT category, SUM(amount) as total
    FROM expenses
    WHERE expense_date BETWEEN "2024-08-01" and "2024-08-05"
    GROUP BY category;
    '''
    with get_db_cursor() as cursor:
        # cursor.execute('SELECT category, SUM(amount) as total FROM expenses WHERE expense_date BETWEEN "2024-08-01" and "2024-08-05" GROUP BY category;')
        cursor.execute(
            '''SELECT category, SUM(amount) as total
            FROM expenses
            WHERE expense_date BETWEEN %s and %s
            GROUP BY category;''', (start_date, end_date)
        )
        data = cursor.fetchall()
        print(data)
    return data




if __name__ == "__main__":
    # expenses = fetch_expenses_for_date("2024-08-07")
    # print(expenses)
    # insert_expenses("2024-08-01", 20, "Shopping", "Bought dairy milk chocolate")
    # print("after")
    # expenses = fetch_expenses_for_date("2024-08-01")
    # print(expenses)
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)








