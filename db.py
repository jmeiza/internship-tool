import sqlite3

# Function to create the database
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

# Function to add a new application
def add_application(comapny, role, date_applied):
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO applications (company, role, date_applied, status) VALUES (?, ?, ?, ?)", (comapny, role, date_applied, "drafted")
    )

    conn.commit()
    conn.close()

# Function to get all the applications
def get_all_applications():
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM applications")

    rows = cur.fetchall()
    conn.close()
    return rows

# Function to update the status of a specific application
def update_status(id, new_status):
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE applications SET status = ? WHERE id = ?", (new_status, id)
    )
    conn.commit()
    conn.close()

# Function to update the follow_up date of an application
def update_follow_up_date(id, new_follow_up_date):
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE applications SET follow_up_date = ? WHERE id = ?", (new_follow_up_date, id)
    )
    conn.commit()
    conn.close()


# Function to get a specific application
def get_application(id):
    conn = sqlite3.connect("JobTracker.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM applications WHERE id = ?", (id,)
    ) 
    row = cur.fetchone()
    conn.close()
    return row

if __name__ == "__main__":
    init_db()
    add_application("Google", "SWE Intern", "2026-08-04")

