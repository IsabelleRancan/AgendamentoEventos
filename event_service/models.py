import sqlite3

def init_db():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            max_participants INTEGER NOT NULL,
            registered_participants INTEGER NOT NULL DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            participant_email TEXT NOT NULL,
            FOREIGN KEY (event_id) REFERENCES events (id)
        )
    ''')

    conn.commit()
    conn.close()
