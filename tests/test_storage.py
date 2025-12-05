from tasksync.models import Task
from tasksync.storage import DB_PATH, get_connection, init_db, load_data
import unittest
import os

class testStorage(unittest.TestCase):
    def testInit(self):
        init_db()
        self.assertTrue(os.path.exists(DB_PATH))
        
        conn = get_connection()
        db = conn.cursor()

        db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
        result = db.fetchone()

        self.assertTrue(result is not None)
        
        PY_TO_SQL = {
            int: "INTEGER",
            str: "TEXT",
            float: "REAL",
            bytes: "BLOB",
            bool: "INTEGER",
        }
        annotations = Task.__annotations__
        expected_sql = {
            name: PY_TO_SQL.get(tp, "TEXT")
            for name, tp in annotations.items()
        }
        db.execute(f"PRAGMA table_info(tasks)")
        rows = db.fetchall()
        actual = {r[1]: r[2] for r in rows}
        normalize = lambda t: t.upper().split("(")[0]
        actual_norm = {k: normalize(v) for k, v in actual.items()}
        self.assertEqual(expected_sql, actual_norm)

        conn.commit()
        conn.close()