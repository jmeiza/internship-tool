import sqlite3

def init_db():
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS applications (" \
    "id INTEGER PRIMARY KEY AUTOINCREMENT," \
    "company TEXT NOT NULL," \
    "role TEXT NOT NULL," \
    "date_applied TEXT NOT NULL," \
    "status TEXT NOT NULL," \
    "follow_up_date TEXT)")

    conn.commit()
    conn.close()

def add_application(comapny, role, date_applied):
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO applications (company, role, date_applied, status) VALUES (?, ?, ?, ?)", (comapny, role, date_applied, "drafted")
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    add_application("Google", "SWE Intern", "2026-08-04")

