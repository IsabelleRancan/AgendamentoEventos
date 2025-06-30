from db import get_connection

def create_event(event):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO events (title, description, date, max_participants, registered_participants)
        VALUES (?, ?, ?, ?, 0)
    ''', (event['title'], event['description'], event['date'], event['max_participants']))
    conn.commit()
    conn.close()

def get_all_events():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events')
    events = cursor.fetchall()
    conn.close()
    return events

def get_upcoming_events():
    import datetime
    today = datetime.date.today().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events WHERE date > ?', (today,))
    events = cursor.fetchall()
    conn.close()
    return events

def get_event_by_id(event_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM events WHERE id = ?', (event_id,))
    event = cursor.fetchone()
    conn.close()
    return event

def is_event_full(event_id):
    event = get_event_by_id(event_id)
    if event is None:
        return True  # Considera como "cheio" se não existe
    max_participants = event[4]
    registered = event[5]
    return registered >= max_participants

def register_participant(event_id, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO subscriptions (event_id, participant_email)
        VALUES (?, ?)
    ''', (event_id, email))
    
    cursor.execute('''
        UPDATE events
        SET registered_participants = registered_participants + 1
        WHERE id = ?
    ''', (event_id,))
    
    conn.commit()
    conn.close()
