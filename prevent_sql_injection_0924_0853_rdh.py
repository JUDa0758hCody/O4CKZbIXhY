# 代码生成时间: 2025-09-24 08:53:10
import sqlite3
from sqlite3 import Error
import gradio as gr

"""
This script is designed to demonstrate how to prevent SQL Injection attacks using Python and Gradio.
It creates a simple program where users can input a query to retrieve data from a SQLite database.
The query is sanitized to prevent SQL injection.
"""

# Function to connect to SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

# Function to execute a query and return the result
def execute_query(conn, query, params):
    try:
        cur = conn.cursor()
        cur.execute(query, params)
        result = cur.fetchall()
        return result
    except Error as e:
        print(e)
        return None

# Function to prevent SQL injection by parameterized queries
def safe_query(conn, query, params):
    results = []
    try:
        results = execute_query(conn, query, params)
    except Exception as e:
        print("Error: ", e)
    return results

# Gradio interface
def gr_sql_interface(query_param):
    database = "example.db"  # Path to the SQLite database
    conn = create_connection(database)
    if conn is not None:
        # Sanitize the user input to prevent SQL injection
        query = f"SELECT * FROM employees WHERE name=?"
        params = (query_param,)
        results = safe_query(conn, query, params)
        conn.close()
        return results
    else:
        return "Error: Connection to database failed."

iface = gr.Interface(
    gr_sql_interface,
    "text",
    "json",
    inputs=gr.Textbox(label="Enter Name")),
    outputs=gr.Dropdown(label="Results"))

if __name__ == '__main__':
    iface.launch()
