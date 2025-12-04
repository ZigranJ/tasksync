from .models import Task
import os
import sqlite3
import logging

DB_PATH = "tasks.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    logging.info("Initializing database.")
    conn = get_connection()
    db = conn.cursor()

    db.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            name TEXT PRIMARY KEY,
            project TEXT,
            done INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

def load_data():
    logging.info("Loading database.")
    conn = get_connection()
    db = conn.cursor()

    db.execute("SELECT name, project, done FROM tasks")
    rows = db.fetchall()
    conn.close()

    return [Task(name=row[0], project=row[1] or "", done=bool(row[2])) for row in rows]